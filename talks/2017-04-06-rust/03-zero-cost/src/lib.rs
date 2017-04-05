#![feature(test)]

extern crate test;

pub fn inner_prod_unrolled(x1: u32,
                           x2: u32,
                           x3: u32,
                           x4: u32,
                           y1: u32,
                           y2: u32,
                           y3: u32,
                           y4: u32)
                           -> u32 {
    x1 * y1 + x2 * y2 + x3 * y3 + x4 * y4
}

pub fn inner_prod_slices_zip(xs: &[u32], ys: &[u32]) -> u32 {
    xs.iter().zip(ys).map(|(x, y)| x * y).sum()
}

pub fn inner_prod_slices_iter(xs: &[u32], ys: &[u32]) -> u32 {
    let mut ix = xs.iter();
    let mut iy = ys.iter();
    let mut sum = 0;
    loop {
        sum += match ix.next() {
            Some(x) => {
                match iy.next() {
                    Some(y) => x * y,
                    None => break,
                }
            }
            None => break,
        }
    }

    sum
}

pub fn inner_prod_slices_for(xs: &[u32], ys: &[u32]) -> u32 {
    let mut sum = 0;
    for i in 0..xs.len() {
        sum += xs[i] * ys[i];
    }

    sum
}

#[cfg(test)]
mod tests {
    use super::*;


    #[test]
    fn test_unrolled() {
        assert_eq!(inner_prod_unrolled(10, 20, 30, 40, 50, 60, 70, 80), 7000);
    }

    #[test]
    fn test_slices_zip() {
        let xs = &[10, 20, 30, 40];
        let ys = &[50, 60, 70, 80];
        assert_eq!(inner_prod_slices_zip(xs, ys), 7000);
    }

    #[test]
    fn test_slices_iter() {
        let xs = &[10, 20, 30, 40];
        let ys = &[50, 60, 70, 80];
        assert_eq!(inner_prod_slices_iter(xs, ys), 7000);
    }

    #[test]
    fn test_slices_for() {
        let xs = &[10, 20, 30, 40];
        let ys = &[50, 60, 70, 80];
        assert_eq!(inner_prod_slices_for(xs, ys), 7000);
    }

    #[bench]
    fn bench_unrolled(b: &mut test::Bencher) {
        let (x1, x2, x3, x4) = (1, 2, 3, 4);
        let (y1, y2, y3, y4) = (5, 6, 7, 8);
        b.iter(|| {
            inner_prod_unrolled(test::black_box(x1),
                                test::black_box(x2),
                                test::black_box(x3),
                                test::black_box(x4),
                                test::black_box(y1),
                                test::black_box(y2),
                                test::black_box(y3),
                                test::black_box(y4))
        })
    }

    #[bench]
    fn bench_slices_4(b: &mut test::Bencher) {
        let xs = (1..5).collect::<Vec<u32>>();
        let ys = (5..9).collect::<Vec<u32>>();
        b.iter(|| {
            inner_prod_slices_zip(test::black_box(&xs), test::black_box(&ys))
        });
    }

    #[bench]
    fn bench_slices_zip(b: &mut test::Bencher) {
        let xs = (1000..2000).collect::<Vec<u32>>();
        let ys = (2000..3000).collect::<Vec<u32>>();
        b.iter(|| {
            inner_prod_slices_zip(test::black_box(&xs), test::black_box(&ys))
        });
    }

    #[bench]
    fn bench_slices_iter(b: &mut test::Bencher) {
        let xs = (1000..2000).collect::<Vec<u32>>();
        let ys = (2000..3000).collect::<Vec<u32>>();
        b.iter(|| {
            inner_prod_slices_iter(test::black_box(&xs), test::black_box(&ys))
        });
    }

    #[bench]
    fn bench_slices_for(b: &mut test::Bencher) {
        let xs = (1000..2000).collect::<Vec<u32>>();
        let ys = (2000..3000).collect::<Vec<u32>>();
        b.iter(|| {
            inner_prod_slices_for(test::black_box(&xs), test::black_box(&ys))
        });
    }
}
