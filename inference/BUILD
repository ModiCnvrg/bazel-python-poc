# load("@infaas_deps//:requirements.bzl", "requirement")
load("@infaas_deps//:requirements.bzl", "requirement")

py_library(
    name = "svc",
    deps = [
        "@infaas_deps//flask",
        "@infaas_deps//transformers",
        "@infaas_deps//torch",
    ], 
)

py_binary(
    name = "run_app",
    srcs = [
        "app.py",
        ],
    deps = [
        ":svc",
    ],
    main = "app.py",
)

py_binary(
    name = "print_env",
    srcs = ["print_env.py"],
    main = "print_env.py",
    deps = [
        ":svc",
        requirement("setuptools"),  # Ensure setuptools is included for pkg_resources
    ],
)