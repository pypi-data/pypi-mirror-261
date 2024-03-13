use pyo3::prelude::*;
use std::cmp::min;

/// Calculate the levenshtein distance between the words of two strings
// Modified version of https://github.com/wooorm/levenshtein-rs
// MIT license: Copyright (c) 2016 Titus Wormer <tituswormer@gmail.com>
#[pyfunction]
fn levenshtein_list(a: Vec<&str>, b: Vec<&str>) -> usize {
    let mut result = 0;

    /* Shortcut optimizations / degenerate cases. */
    if a == b {
        return result;
    }

    let length_a = a.len();
    let length_b = b.len();

    if length_a == 0 {
        return length_b;
    }

    if length_b == 0 {
        return length_a;
    }

    /* Initialize the vector.
     *
     * This is why it’s fast, normally a matrix is used,
     * here we use a single vector. */
    let mut cache: Vec<usize> = (1..).take(length_a).collect();
    let mut distance_a;
    let mut distance_b;

    /* Loop. */
    for (index_b, code_b) in b.iter().enumerate() {
        result = index_b;
        distance_a = index_b;

        for (index_a, code_a) in a.iter().enumerate() {
            distance_b = if code_a == code_b {
                distance_a
            } else {
                distance_a + 1
            };

            distance_a = cache[index_a];

            result = if distance_a > result {
                if distance_b > result {
                    result + 1
                } else {
                    distance_b
                }
            } else if distance_b > distance_a {
                distance_a + 1
            } else {
                distance_b
            };

            cache[index_a] = result;
        }
    }

    result
}

/// reference levenshtein function
/// see https://en.wikipedia.org/wiki/Levenshtein_distance#Definition
fn levenshtein_ref(a: &[&str], b: &[&str]) -> usize {
    if a.is_empty() {
        return b.len();
    }
    if b.is_empty() {
        return a.len();
    }

    if a[0] == b[0] {
        return levenshtein_ref(&a[1..], &b[1..]);
    }
    1 + min(
        levenshtein_ref(&a[1..], &b[1..]),
        min(levenshtein_ref(a, &b[1..]), levenshtein_ref(&a[1..], b)),
    )
}

/// A Python module implemented in Rust.
#[pymodule]
fn levenshtein_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(crate::levenshtein_list, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn basic_test() {
        let a = ["mary", "had", "a", "little", "lamb"];
        let b = ["bob", "had", "a", "little", "foal"];
        let c = ["just", "some", "text"];
        assert_eq!(super::levenshtein_ref(&a, &b), 2);
        assert_eq!(super::levenshtein_ref(&a, &a), 0);
        assert_eq!(super::levenshtein_ref(&a, &c), 5);
    }

// Now let's use proptest
    use proptest::prelude::*;

    proptest! {
        #[test]
        fn test_levenshtein(a in ".*", b in ".*") {
            let a = a.split_whitespace().collect::<Vec<&str>>();
            let b = b.split_whitespace().collect::<Vec<&str>>();
            assert_eq!(super::levenshtein_ref(&a, &b), super::levenshtein_ref(&b, &a));
            assert_eq!(super::levenshtein_ref(&a, &b), super::levenshtein_list(a, b));
        }
    }

}
