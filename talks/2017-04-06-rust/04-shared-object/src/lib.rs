use std::slice;

#[no_mangle]
pub extern "C" fn max_byte(base: *const u8, len: usize) -> u8 {
    let buf = unsafe {
        assert!(!base.is_null());
        slice::from_raw_parts(base, len)
    };
    *buf.iter().max().unwrap_or(&0)
}
