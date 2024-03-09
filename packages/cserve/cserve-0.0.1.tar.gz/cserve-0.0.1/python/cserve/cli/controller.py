# Copyright (c) CentML Inc. All Rights Reserved.
""" CLI for CServe Controller """
from cserve.controller.api import list_apis


def add_controller_parser(subparsers):
    """Add controller parser"""
    controller_parser = subparsers.add_parser('controller')

    controller_subparsers = controller_parser.add_subparsers(title='Subcommands', dest='controller_sub')
    start_parser = controller_subparsers.add_parser(
        'start', description="start the controller service against a list of engines"
    )
    start_parser.add_argument(
        "--host", type=str, default="localhost", help="what host to listen to (default: localhost)"
    )
    start_parser.add_argument(
        "--api_type",
        type=str,
        default=None,
        choices=list_apis(),
        help="only expose this API type, default to expose all",
    )
    start_parser.add_argument("--port", type=int, default=8080, help="port of the http endpoint")
    start_parser.add_argument("--plan", type=str, help="path to a deployment plan file generated from cserve plan")
    start_parser.add_argument(
        "--engine_managers",
        type=str,
        default=None,
        nargs='*',
        help="host:port(s) of engine manager(s) if different from the plan file",
    )
    start_parser.add_argument(
        "--engines", type=str, default=None, nargs='*', help="Overwrites engines to bind to from plan file"
    )
    start_parser.add_argument(
        "--distributed-init-method", type=str, default=None, help="distributed init method, e.g. tcp://localhost:10021"
    )
    start_parser.add_argument("--foreground", action='store_true', help="run the controller in foreground mode")

    stop_parser = controller_subparsers.add_parser('stop', description="stop controller(s)")
    stop_parser.add_argument("--all", action='store_true', help="stop all controller services")
    stop_parser.add_argument("controller_ids", type=int, nargs='*', help="the id of the controller service to stop")

    controller_subparsers.add_parser('status', description="list the status of all running controllers")


def run(args):
    """Run the controller service based on user provided CLI args"""
    from cserve.controller.service import ControllerService, ControllerArgs

    controller_args = ControllerArgs.from_args(args)
    controller_service = ControllerService(controller_args)
    if args.controller_sub == 'start':
        controller_service.start()
    elif args.controller_sub == 'stop':
        controller_service.stop()
    elif args.controller_sub == 'status':
        controller_service.status()
    else:
        raise NotImplementedError()
