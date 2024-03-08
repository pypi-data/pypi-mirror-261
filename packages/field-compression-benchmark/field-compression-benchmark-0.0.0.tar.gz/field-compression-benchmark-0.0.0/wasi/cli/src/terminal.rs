use crate::{
    bindings::exports::wasi::cli::{
        terminal_input::TerminalInput, terminal_output::TerminalOutput,
        terminal_stderr::Guest as WasiCliTerminalStderr,
        terminal_stdin::Guest as WasiCliTerminalStdin,
        terminal_stdout::Guest as WasiCliTerminalStdout,
    },
    VirtCli,
};

impl WasiCliTerminalStdin for VirtCli {
    fn get_terminal_stdin() -> Option<TerminalInput> {
        None
    }
}

impl WasiCliTerminalStdout for VirtCli {
    fn get_terminal_stdout() -> Option<TerminalOutput> {
        None
    }
}

impl WasiCliTerminalStderr for VirtCli {
    fn get_terminal_stderr() -> Option<TerminalOutput> {
        None
    }
}
