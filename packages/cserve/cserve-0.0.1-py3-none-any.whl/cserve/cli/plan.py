# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Copyright (c) CentML Inc. All Rights Reserved.
from cserve.utils.cache import cache_dir, CACHE_DIR


def add_plan_parser(subparsers):
    plan_parser = subparsers.add_parser('plan')

    # Model configs
    plan_parser.add_argument("--model", type=str, required=True, help="path of the model (HF hub or local)")
    plan_parser.add_argument(
        "--is_embedding_model", action='store_true', help="whether the model is an embedding model"
    )
    plan_parser.add_argument(
        "--tokenizer", type=str, default=None, help="path of tokenizer, if left unspecified" "set to same as the model"
    )
    plan_parser.add_argument("--ngpus", type=int, default=None, help="total number of GPUs to use for the deployment")
    plan_parser.add_argument("--tensor_parallel_size", type=int, default=None, help="tensor parallel size")
    plan_parser.add_argument("--pipeline_parallel_size", type=int, default=None, help="pipeline parallel size")
    plan_parser.add_argument(
        '--gpu_mem_util', type=float, default=0.9, help="amount of memory usable per GPU (from 0 to 1)"
    )
    plan_parser.add_argument('--quantization', '-q', choices=['awq'], default=None, help="quantization mode")
    plan_parser.add_argument(
        "--sampling", choices=["beam_search", "default"], default='default', help="Sampling technique to use"
    )
    plan_parser.add_argument(
        "--num_samples", type=int, default=1, help="How many completions to generate in parallel for a single prompt"
    )
    plan_parser.add_argument(
        '--dtype',
        type=str,
        default='auto',
        choices=['auto', 'half', 'float16', 'bfloat16', 'float', 'float32'],
        help='data type for model weights and activations. '
        'The "auto" option will use FP16 precision '
        'for FP32 and FP16 models, and BF16 precision '
        'for BF16 models.',
    )
    plan_parser.add_argument(
        '--cache_dtype',
        type=str,
        default='auto',
        choices=['auto', 'fp8_e5m2'],
        help='Data type for kv cache storage. If "auto", will use model '
        'data type. Note FP8 is not supported when cuda version is '
        'lower than 11.8.',
    )
    plan_parser.add_argument(
        "--cudagraph", action='store_true', default=False, help="Whether to enable CUDAGraph for model execution"
    )

    plan_parser.add_argument('--interval', type=float, default=10.0, help="time to issue request from")
    plan_parser.add_argument('--max_reqs', type=int, default=None, help="maximum number of requests to generate")
    np_rand_functions = [
        'beta',
        'gamma',
        'binomial',
        'chisquare',
        'exponential',
        'geometric',
        'uniform',
        'normal',
        'laplace',
        'poisson',
        'logistic',
    ]
    plan_parser.add_argument(
        '--input_dist',
        type=str,
        default='uniform',
        choices=np_rand_functions,
        help="distribution of input (prefill) lengths, default uniform from 128 to 1024",
    )
    plan_parser.add_argument(
        '--output_dist',
        type=str,
        default='uniform',
        choices=np_rand_functions,
        help="distribution of output (decoding) lengths, default uniform from 1 to 255",
    )
    plan_parser.add_argument(
        '--request_dist',
        type=str,
        default="exponential",
        choices=np_rand_functions,
        help="distribution of interval between requests, default exponential",
    )
    plan_parser.add_argument(
        '--input_dist_kwargs',
        type=str,
        default='{"low":128, "high":1024}',
        help="kwargs in the form of dict for input distribution function, see numpy.random.*",
    )
    plan_parser.add_argument(
        '--output_dist_kwargs',
        type=str,
        default='{"low":1, "high":255}',
        help="kwargs in the form of dict for output distribution function, see numpy.random.*",
    )
    plan_parser.add_argument(
        '--request_dist_kwargs',
        type=str,
        default='{"scale":0.1}',
        help="kwargs in the form of dict for request interval distribution function, see numpy.random.*"
        "default is {\"scale\": 0.1}, intended to be passed to np.random.exponential",
    )

    plan_parser.add_argument('--plan_file', type=str, default=None, help="destination of the plan file generated")

    plan_parser.add_argument("--seed", type=int, default=0, help="seed for load generation")
    plan_parser.add_argument("--tensorboard", action='store_true', help="render the results using tensorboard")
    plan_parser.add_argument(
        "--tensorboard_port",
        type=int,
        default=6006,
        help="port to launch or connect the tensorboard instance, default is 6006",
    )
    plan_parser.add_argument(
        "--tensorboard_logdir",
        type=str,
        default=cache_dir("plan_tb_logdir"),
        help="logdir for tensorboard," "default is under {}/plan_tb_logdir".format(CACHE_DIR),
    )

    plan_parser.add_argument(
        "--engine_managers", type=str, nargs="+", help="ip and port to connect to CServe manager HTTP server"
    )

    plan_parser.add_argument(
        "--use_flashinfer", action='store_true', default=False, help="whether to use flashinfer for attention ops"
    )


def run(args):
    from cserve.plan import plan_from_args

    plan_from_args(args)
