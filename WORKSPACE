load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


# Update the SHA and VERSION to the lastest version available here:
# https://github.com/bazelbuild/rules_python/releases.

SHA="f4770504f74b9ef87984224a06df35b931d35a2e695ea898102bd9df30ce4fe6"

VERSION="0.32.0"

http_archive(
    name = "rules_python",
    sha256 = SHA,
    strip_prefix = "rules_python-{}".format(VERSION),
    url = "https://github.com/bazelbuild/rules_python/releases/download/{}/rules_python-{}.tar.gz".format(VERSION,VERSION),
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python_3_11",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.11",
)

load("@python_3_11//:defs.bzl", interpreter_3_11 = "interpreter")

load("@rules_python//python:pip.bzl", "pip_parse")

# Create a central repo that knows about the dependencies needed from
# requirements_lock.txt.
pip_parse(
   name = "infaas_deps",
   requirements_lock = "//inference:requirements_lock.txt",
   python_interpreter_target = interpreter_3_11,
   download_only = True,
)
# Load the starlark macro, which will define your dependencies.
load("@infaas_deps//:requirements.bzl", "install_deps")
# Call it to define repos for your requirements.
install_deps()