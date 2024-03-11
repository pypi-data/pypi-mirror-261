# ruff: noqa: D100, D101, D102, D103, D104, D107
import os
import sys
import threading
import traceback
from types import TracebackType

from redux import FinishAction

from ubo_app.constants import GUI_LOG_LEVEL, LOG_LEVEL


def main() -> None:
    """Instantiate the `MenuApp` and run it."""
    if LOG_LEVEL:
        import logging

        import ubo_app.logging

        level = getattr(
            ubo_app.logging,
            LOG_LEVEL,
            getattr(logging, LOG_LEVEL, logging.INFO),
        )

        ubo_app.logging.logger.setLevel(level)
        ubo_app.logging.add_file_handler(ubo_app.logging.logger, level)
        ubo_app.logging.add_stdout_handler(ubo_app.logging.logger, level)
    if GUI_LOG_LEVEL:
        import logging

        import ubo_gui.logger

        level = getattr(
            ubo_gui.logger,
            GUI_LOG_LEVEL,
            getattr(logging, GUI_LOG_LEVEL, logging.INFO),
        )

        ubo_gui.logger.logger.setLevel(level)
        ubo_gui.logger.add_file_handler(level)
        ubo_gui.logger.add_stdout_handler(level)

    if len(sys.argv) > 1 and sys.argv[1] == 'bootstrap':
        from ubo_app.system.bootstrap import bootstrap

        bootstrap(
            with_docker='--with-docker' in sys.argv,
            for_packer='--for-packer' in sys.argv,
        )
        sys.exit(0)

    def global_exception_handler(
        exception_type: type,
        value: int,
        tb: TracebackType,
    ) -> None:
        from ubo_app.logging import logger

        logger.error(f'Uncaught exception: {exception_type}: {value}')
        logger.error(''.join(traceback.format_tb(tb)))

    # Set the global exception handler
    sys.excepthook = global_exception_handler

    def thread_exception_handler(args: threading.ExceptHookArgs) -> None:
        import traceback

        from ubo_app.logging import logger

        logger.error(
            f"""Exception in thread {args.thread.name if args.thread else "-"}: {
            args.exc_type} {args.exc_value}""",
        )
        logger.error(''.join(traceback.format_tb(args.exc_traceback)))

    threading.excepthook = thread_exception_handler

    import headless_kivy_pi.config

    os.environ['KIVY_METRICS_DENSITY'] = '1'
    os.environ['KIVY_NO_CONFIG'] = '1'
    os.environ['KIVY_NO_FILELOG'] = '1'
    headless_kivy_pi.config.setup_headless_kivy({'automatic_fps': True})

    from kivy.clock import Clock

    from ubo_app.load_services import load_services
    from ubo_app.menu import MenuApp

    # Needed since redux is scheduled using Clock scheduler and Clock doesn't run before
    # app is running
    Clock.tick()

    load_services()

    app = MenuApp()

    try:
        app.run()
    finally:
        from ubo_app.store import dispatch

        dispatch(FinishAction())

        # Needed since redux is scheduled using Clock scheduler and Clock doesn't run
        # after app is stopped.
        Clock.tick()


if __name__ == '__main__':
    main()
