from setuptools import setup

setup(
    name="devpi-client-password-stdin",
    install_requires="devpi-client",
    entry_points={"devpi_client": ["devpi-client-password-stdin = devpi_client_password_stdin"]},
    py_modules=["devpi_client_password_stdin"],
)
