# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Copyright (c) CentML Inc. All Rights Reserved.


def add_engine_parser(subparsers):
    engine_parser = subparsers.add_parser('engine')

    engine_subparser = engine_parser.add_subparsers(title='Subcommands', dest='engine_sub')
    start_parser = engine_subparser.add_parser(
        'start', description="start the engine gRPC service attached to a specific GPU"
    )
    start_parser.add_argument("gpu_id", type=int, help="the GPU index that this engine runs on")
    start_parser.add_argument(
        "--host", type=str, default="localhost", help="what host to listen to (default: localhost)"
    )
    start_parser.add_argument("--port", type=int, default=50051, help="port of the gRPC service")
    start_parser.add_argument("--foreground", action='store_true', help="run the engine in foreground mode")

    engine_subparser.add_parser('status')

    stop_parser = engine_subparser.add_parser('stop')
    stop_parser.add_argument("gpu_id", type=int, nargs='+', help="the list of engines to stop")

    manager_parser = engine_subparser.add_parser('manager', description="Engine manager from file")
    manager_parser.add_argument("engine_manager_file", type=str, help="yaml file of the engine manager configuration")
    manager_parser.add_argument(
        "--manager_port", type=int, default=None, help="an alternative port for engine manager if specified"
    )


def run(args):
    if args.engine_sub == 'start':
        # from cserve.engine.service import launch_engine
        from cserve.engine import launch_engine

        launch_engine(args.gpu_id, args.host, args.port, args.foreground)

    elif args.engine_sub == 'status':
        from cserve.engine import check_status_all

        check_status_all()

    elif args.engine_sub == 'stop':
        from cserve.engine import kill_engine

        kill_engine(args.gpu_id)

    elif args.engine_sub == 'manager':
        from cserve.engine.manager import start_manager

        start_manager(args.engine_manager_file, args.manager_port)

    else:
        raise NotImplementedError()
