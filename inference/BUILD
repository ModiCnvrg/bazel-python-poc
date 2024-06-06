# load("@infaas_deps//:requirements.bzl", "requirement")
load("@infaas_deps//:requirements.bzl", "requirement")

# Define a filegroup for the model files
filegroup(
    name = "model_files",
    srcs = glob(["model/**/*"]),
)

py_library(
    name = "svc",
    deps = [
        requirement("flask"),
        requirement("transformers"),
        requirement("torch"),
    ],
)

py_binary(
    name = "run_app",
    srcs = [
        "app.py",
        ],
    data = [":model_files"],  # Include the model files
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