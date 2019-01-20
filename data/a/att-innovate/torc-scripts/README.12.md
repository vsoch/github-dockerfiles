-- Cross-compile a project for Ubuntu
Replace YOUR_RUST_PROJECT_PATH with the full path to your rust project

$ docker run -v YOUR_RUST_PROJECT_PATH:/project/ cargo build

The binary will be in YOUR_RUST_PROJECT_PATH/target/debug
