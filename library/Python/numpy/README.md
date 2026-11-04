# 100 NumPy Programs

One hundred programs that `import numpy as np`, in 10 topics of 10: array
creation, dtypes, indexing, boolean and fancy indexing, broadcasting, ufuncs,
reductions and statistics, reshaping, sorting and sets, and linear algebra.
They print arrays the way NumPy users do (`print(a)`, `repr(a)`), so they also
test NumPy's array printing.

Every program:

- runs with CPython 3.13 and NumPy 2.4 and exits cleanly with nothing on stderr,
- is deterministic (no `np.random`; "random-looking" data comes from a small
  generator written in the program) and prints its results,
- uses int64, float64 and bool arrays (smaller int and float types only in
  `02_dtypes_and_attributes`), and reads no input and writes no files.

The Quantum compiler runs them with its own NumPy (`src/python/lib/numpy.sa`),
and their output is identical to real NumPy's.

```bash
python 05_arithmetic_broadcasting/02_scalar_operations.py   # the reference (NumPy)
qrun 05_arithmetic_broadcasting/02_scalar_operations.py     # Quantum
quantum --test examples                                     # the whole examples tree
```

## 01_array_creation/ — Array creation (10 programs)

- `01_from_lists.py` — Builds 1-D, 2-D and 3-D arrays from lists, tuples and nested lists with np.array and np.asarray.
- `02_zeros_ones_full.py` — Creates constant-filled arrays with zeros, ones and full, including a bordered canvas and an accumulator.
- `03_arange.py` — Generates integer and float sequences with arange, reshapes them into tables and broadcasts a multiplication table.
- `04_linspace.py` — Samples evenly spaced points with linspace, covering endpoint=False, retstep, dtype=int and a trapezoid integral.
- `05_eye_identity_diag.py` — Constructs identity, offset-eye and tridiagonal matrices and builds/extracts diagonals with np.diag.
- `06_like_functions.py` — Uses zeros_like, ones_like and full_like to create arrays matching another array's shape and dtype.
- `07_tile_repeat.py` — Replicates data with tile and repeat along axes to upscale an image, draw a checkerboard and label groups.
- `08_fromfunction_meshgrid.py` — Builds arrays from index formulas with fromfunction and evaluates functions over meshgrid coordinates.
- `09_tri_tril_triu.py` — Works with triangular matrices via tri, tril and triu, including symmetrizing and unique pair distances.
- `10_copy_vs_view.py` — Contrasts views (slices, reshape, transpose, strides) with copies (copy, fancy and boolean indexing).

## 02_dtypes_and_attributes/ — Dtypes and array attributes (10 programs)

- `01_array_attributes.py` — Prints shape, ndim, size, dtype, itemsize, nbytes and T for arrays of rank 0 through 3.
- `02_astype_conversions.py` — Converts between int64, float64 and bool with astype, showing truncation, rounding and copy semantics.
- `03_dtype_in_constructors.py` — Passes dtype= to array, zeros, ones, arange, full and eye and lists dtype kinds and item sizes.
- `04_integer_overflow.py` — Demonstrates wrap-around overflow in uint8, int8 and int16 arithmetic and casts, plus a saturating alternative.
- `05_iinfo_finfo.py` — Queries integer and float limits with iinfo and finfo to pick the smallest fitting type and reason about epsilon.
- `06_type_promotion.py` — Explores promotion rules for mixed int/float/bool operations, result_type, promote_types and weak Python scalars.
- `07_can_cast.py` — Builds a safe-cast table with np.can_cast and compares the no, equiv, safe, same_kind and unsafe casting rules.
- `08_array_scalars.py` — Inspects np.int64/np.float64 array scalars, their repr and type, and how they mix with Python numbers.
- `09_item_and_tolist.py` — Extracts native Python values with .item() and .tolist() to build plain data structures from arrays.
- `10_image_dtype_pipeline.py` — Runs a small LCG-generated grayscale image through uint8, float32, float64 and bool stages.

## 03_indexing_slicing/ — Indexing and slicing (10 programs)

- `01_basic_1d_indexing.py` — Positive/negative indices, stepped and reversed slices, slice objects and a shifted-slice moving average on a 1-D array.
- `02_2d_rows_columns.py` — Element, row, column, sub-block and strided sub-grid selection in a 2-D grid, including diagonals and result shapes.
- `03_3d_ellipsis_newaxis.py` — 3-D indexing with `...`, `np.newaxis`/`None` for adding axes, outer products and pairwise distances via broadcasting.
- `04_views_inplace_modification.py` — Slices, reshapes and ravels as views: writing through them, nested views, `np.shares_memory` and `out=` on a slice.
- `05_copy_vs_view.py` — `np.copy`/`.copy()` vs views, `np.array` vs `np.asarray`, accidental aliasing bugs and contiguity of copies.
- `06_slice_assignment_broadcasting.py` — Slice assignment with scalars, rows, columns and broadcasting: canvases, checkerboards, frames, row/column swaps and dtype truncation.
- `07_flip_and_mirror.py` — `np.flip`, `np.fliplr`, `np.flipud` and `[::-1]` for reversing, mirroring images, palindrome checks and reverse cumulative sums.
- `08_roll_shifts.py` — Circular shifts with `np.roll` in 1-D/2-D, periodic finite differences, a Game-of-Life neighbour count and circular smoothing.
- `09_take_along_axes.py` — `np.take` with axis and `wrap`/`clip` modes, ranking by `argsort`, and `np.take_along_axis` for per-row picks.
- `10_matrix_patch_extraction.py` — Extracting tiles, clipped neighbourhood patches, clockwise borders and pooled blocks from an LCG-generated 2-D field.

## 04_boolean_fancy_indexing/ — Boolean and fancy indexing (10 programs)

- `01_boolean_masks.py` — Building masks from comparisons and using them to filter 1-D data, 2-D grids, rows, columns and outliers.
- `02_combining_masks.py` — Combining masks with `&`, `|`, `~`, `^`, the `np.logical_*` functions and `logical_and.reduce`, plus a contingency table.
- `03_where_three_arg.py` — `np.where` in 1-arg (index) and 3-arg (choice) forms: sign, flooring, safe division with NaN and piecewise functions.
- `04_nonzero_argwhere_count.py` — `np.nonzero`, `np.argwhere`, `np.flatnonzero` and `np.count_nonzero` for sparse coordinates and run detection.
- `05_fancy_integer_indexing.py` — Integer-list/array indexing: permutations and inverses, paired 2-D picks, broadcast indices, one-hot encoding and palette lookup.
- `06_ix_mesh_selection.py` — Cross-product row/column selection with `np.ix_` on a distance table, with boolean masks, assignment and 3-D blocks.
- `07_masked_and_fancy_assignment.py` — Assignment through masks and fancy indices, buffered `+=` vs `np.add.at`, `np.putmask` and `np.place`.
- `08_any_all_axis.py` — `np.any`/`np.all` globally and along axes (incl. tuples and `keepdims`) for quiz results, validation and row filtering.
- `09_clip_extract_select.py` — `np.clip` (scalar, per-element and in-place bounds), `np.extract`, `np.compress` and `np.select` for grades and piecewise tax.
- `10_isin_membership.py` — `np.isin` (incl. `invert=True`) on 1-D and 2-D arrays, alongside `unique`, `intersect1d`, `setdiff1d` and `union1d`.

## 05_arithmetic_broadcasting/ — Arithmetic and broadcasting (10 programs)

- `01_elementwise_basics.py` — Elementwise + - * / // % ** between same-shape int, float and 2-D arrays, with int/float promotion.
- `02_scalar_operations.py` — Array-scalar arithmetic for temperature conversion, price discounts and grid scaling, including scalar-on-the-left forms.
- `03_broadcasting_rows_columns.py` — Broadcasting row and column vectors across a sales table, column centering, keepdims row normalization and result shapes.
- `04_outer_operations.py` — Multiplication, modular addition, distance and growth tables built with `[:, None]` broadcasting and `np.outer`.
- `05_inplace_operators.py` — In-place `+= -= *= /= //= %= **=` on float and int arrays, views vs copies, broadcasting in place and the int `/=` casting error.
- `06_integer_vs_true_division.py` — Floor division, modulo and true division with negative operands, `np.divmod`, `np.fmod` and time/digit decomposition.
- `07_ufunc_function_forms.py` — `np.add`/`subtract`/`multiply`/`divide`/`power`/`mod`/`negative` compared with operators, plus `out=` and `where=` arguments.
- `08_comparisons_bool_arrays.py` — Comparison operators producing bool arrays, mask combination with `& | ~`, broadcast thresholds, `any`/`all` and `np.where`.
- `09_equality_tolerance.py` — Exact vs approximate equality with `np.array_equal`, `np.allclose`, `np.isclose`, tolerances, NaN handling and `np.array_equiv`.
- `10_maximum_minimum.py` — Elementwise `np.maximum`/`np.minimum` for ReLU, clamping, drawdown envelopes and broadcast bounds, with `np.fmax` NaN behavior.

## 06_ufuncs_math/ — Math ufuncs (10 programs)

- `01_roots_exponents_logs.py` — `np.sqrt`, `np.exp`, `np.log`/`log2`/`log10` for decay, compound growth, bit counts and geometric means, plus `log1p`/`expm1`/`cbrt`.
- `02_trigonometry.py` — `np.sin`/`cos`/`tan` and their inverses on sampled angles, identities, zero crossings, a rotation matrix and hyperbolic functions.
- `03_polar_coordinates.py` — Cartesian/polar conversion with `np.hypot` and `np.arctan2`, compass bearings, hexagon vertices and `np.degrees`/`np.radians`.
- `04_rounding_modes.py` — `np.floor`, `np.ceil`, `np.trunc`, `np.rint` and `np.round` (half-to-even, decimals) for bucketing, pagination and `np.modf`.
- `05_abs_sign.py` — `np.abs` and `np.sign` for error metrics, direction changes and Manhattan distances, plus `np.fabs` and `np.copysign`.
- `06_special_values.py` — `np.pi`/`np.e`/`np.inf`/`np.nan` detection with `isnan`/`isinf`/`isfinite`, `nan_to_num`, nan-aware reductions and safe division under `np.errstate`.
- `07_cumulative_diff.py` — Running balances, compounding and factorials with `np.cumsum`/`np.cumprod`, higher-order `np.diff`, moving averages and run lengths.
- `08_gcd_lcm.py` — `np.gcd`/`np.lcm` for reducing fractions, schedule alignment, coprime tables, Euler's totient and common denominators.
- `09_square_reciprocal.py` — `np.square` and `np.reciprocal` on floats for variance, RMS, parallel resistance, harmonic means and the Basel series.
- `10_ufunc_methods.py` — `.reduce`, `.accumulate`, `.outer` and `.reduceat` on `np.add`, `np.multiply` and `np.maximum`, with axes, `initial` and `keepdims`.

## 07_reductions_statistics/ — Reductions and statistics (10 programs)

- `01_basic_reductions.py` — sum/prod/min/max/argmin/argmax over a sales table, per axis and with keepdims, plus any/all/count_nonzero.
- `02_mean_std_var.py` — Mean, standard deviation and variance with axis, keepdims and ddof, including z-score normalisation.
- `03_median_percentile_quantile.py` — Median, percentile and quantile (linear method) on latency data, with IQR outlier fences and per-axis order statistics.
- `04_weighted_average_ptp.py` — np.average with weights (and returned=True) for a grade book, plus np.ptp ranges per axis.
- `05_bincount_histogram.py` — np.bincount (minlength, weights) on LCG dice rolls and np.histogram with integer, explicit and ranged bins.
- `06_unique_counts.py` — np.unique with return_counts, return_index and return_inverse for label encoding, plus unique rows via axis=0.
- `07_correlation_covariance.py` — np.cov (ddof/bias, rowvar) and np.corrcoef on small series, checked against a manual Pearson r.
- `08_cumulative_stats.py` — cumsum/cumprod, running max/min via ufunc.accumulate, drawdown, moving and running averages.
- `09_nan_aware_stats.py` — nansum/nanmean/nanmax/nanmin/nanstd/nanmedian/nanpercentile on sensor data with missing values, and mean imputation.
- `10_grade_report_summary.py` — A describe()-style summary report combining percentiles, ranking, histogram letter grades, pass rates and unique buckets.

## 08_reshape_stack_split/ — Reshaping, stacking and splitting (10 programs)

- `01_reshape_basics.py` — reshape with -1 inference, Fortran order, views, and block sums on a 3-D array.
- `02_ravel_flatten.py` — ravel vs flatten (view vs copy), C/F order, .flat, ravel_multi_index and unravel_index.
- `03_transpose_axes.py` — transpose, .T, swapaxes and moveaxis on matrices and image-like 3-D batches.
- `04_expand_squeeze_atleast.py` — expand_dims, np.newaxis, squeeze and atleast_1d/2d/3d for normalising input shapes.
- `05_concatenate_stack.py` — concatenate, stack, vstack, hstack, column_stack and dstack, including building a design matrix.
- `06_split_arrays.py` — split, array_split, hsplit and vsplit for train/validation/test and mini-batch partitioning.
- `07_append_insert_delete.py` — np.append, np.insert and np.delete with and without axis, maintaining a sorted score list.
- `08_padding.py` — np.pad in constant and edge modes for 1-D smoothing, a 2-D box blur and padding ragged sequences.
- `09_broadcast_to.py` — np.broadcast_to, broadcast_arrays and broadcast_shapes, including zero strides and read-only views.
- `10_image_tiles_pipeline.py` — Tiling an image into blocks via reshape/swapaxes, pooling, and reassembling with split, stack and np.block.

## 09_sorting_searching_sets/ — Sorting, searching and sets (10 programs)

- `01_sort_basics.py` — np.sort on 1-D and 2-D arrays along each axis and flattened, descending via `[::-1]`, in-place `ndarray.sort`, floats and booleans.
- `02_argsort_ranking.py` — Ranking students with stable np.argsort, descending ties, inverse-permutation ranks, dense ranks via np.unique, and np.take_along_axis.
- `03_lexsort_multikey.py` — Multi-key table sorting with np.lexsort, lexicographic row ordering, and per-group leaders compared against a stable argsort chain.
- `04_searchsorted_insertion.py` — np.searchsorted with left/right sides for counting, membership, range queries, sorted insertion, `sorter=`, grade cutoffs and CDF buckets.
- `05_partition_topk.py` — k-th order statistics and top-k selection with np.partition/np.argpartition on LCG data, including row- and column-wise variants.
- `06_unique_counts.py` — np.unique with return_counts/return_index/return_inverse, order-preserving unique, unique rows (axis=0) and group-by sums with np.bincount.
- `07_set_operations.py` — Course enrollment set algebra with intersect1d (return_indices), union1d, setdiff1d, setxor1d and np.isin masks (including invert and 2-D).
- `08_digitize_binning.py` — Binning LCG-generated heights with np.digitize (right=True/False, decreasing bins), bincount histograms and comparison with np.histogram.
- `09_leaderboard_argmax.py` — Tournament leaderboard using argmax/argmin per axis, repeated-argmax ranking, np.unravel_index, np.nonzero and np.where.
- `10_merge_and_search.py` — Merging sorted event logs with stable sort, duplicate detection, nearest-neighbour lookup and windowed counts via searchsorted.

## 10_linear_algebra_applications/ — Linear algebra and applications (10 programs)

- `01_matrix_products.py` — np.dot, np.matmul, the `@` operator, batched matmul, np.inner/np.outer and transpose/associativity identities.
- `02_det_inv_solve.py` — np.linalg.det/inv/solve on a 3x3 system, multiple right-hand sides, determinant properties and LinAlgError for a singular matrix.
- `03_norms_rank_trace.py` — Vector L1/L2/max norms, Frobenius and induced matrix norms, pairwise distances, np.linalg.matrix_rank and np.trace with offsets.
- `04_cross_rotation.py` — np.cross for normals and triangle areas, 3-D and 2-D rotation matrices, orthogonality checks and matrix_power of a rotation.
- `05_einsum_basics.py` — np.einsum for matmul, trace, diagonal, row/column sums, transpose, dot/outer products, quadratic forms and batched products.
- `06_markov_chain.py` — Weather Markov chain evolved step by step and with np.linalg.matrix_power, steady state checked against np.linalg.solve, plus Fibonacci powers.
- `07_linear_regression.py` — Least-squares line, quadratic (np.vander) and multi-feature regression via the normal equations and np.linalg.solve, with R^2 and residual checks.
- `08_game_of_life.py` — Conway's Game of Life on a torus using np.roll neighbour counts: glider translation, blinker oscillation and block still life.
- `09_convolution_slicing.py` — 2-D box blur, Sobel edges and Laplacian on a synthetic image via shifted slices, edge padding with np.pad and reshape-based max pooling.
- `10_polynomials_vander.py` — Polynomial evaluation with np.polyval, np.vander and Horner's method, cubic interpolation via solve, and polymul/polydiv/polyder/polyint/poly.

