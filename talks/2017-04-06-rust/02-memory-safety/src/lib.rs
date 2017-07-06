
fn authenticate_user(password: String) -> bool {
    let mut buf: [u8; 10] = [0; 10]; // should be long enough
    let ok = false;

    for (i, b) in password.bytes().enumerate() {
        buf[i] = b;
    }

    // do something with buf

    return ok;
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn overflow() {
        authenticate_user(String::from("long user input..."));
    }

    #[test]
    fn unsafe_overflow() {
        unsafe {
            authenticate_user(String::from("long user input..."));
        }
    }
}
