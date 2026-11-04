# 500 Python Programs

Five hundred self-contained Python programs in 25 topics of 20, from the basics
to dataclasses, algorithms and puzzles. They are written as a Python programmer
would write them, not in a subset chosen for Quantum, so they also measure how
much real Python the compiler runs.

Every program:

- runs in CPython 3.13 and exits cleanly,
- is deterministic (no `random`, clock or input; random-looking data comes from
  a small generator written in the program; sets of strings are sorted before
  printing) and prints its results,
- reads no standard input and writes no files, so `quantum --test` can run it.

```bash
python 16_graphs/04_dijkstra_heapq.py     # the reference
qrun 16_graphs/04_dijkstra_heapq.py       # Quantum
quantum --test examples                   # the whole examples tree
```

They use only these standard modules: `math`, `collections`, `itertools`,
`functools`, `operator`, `re`, `string`, `heapq`, `bisect`, `dataclasses`,
`enum`, `typing`, `fractions`, `decimal`, `json`, `textwrap`, `statistics`,
`copy`, `abc` and `contextlib`.

## 01_basics/ — Basics (20 programs)

- `01_hello_variables.py` — Variables of several types printed with f-strings, swapping, chained assignment and `=` debug specifiers.
- `02_arithmetic_operators.py` — Arithmetic, floor/modulo semantics with negatives, precedence, augmented assignment and chained comparisons.
- `03_temperature_conversion.py` — Temperature conversion functions with an if/elif classifier and a formatted table.
- `04_if_elif_else.py` — Grading, leap years and number classification with if/elif/else plus truthiness of common values.
- `05_for_loops_range.py` — For loops over ranges with steps, a multiplication table, patterns and lazy range objects.
- `06_while_loops.py` — While loops for Collatz, digit sums, GCD, thresholds, and break/continue.
- `07_loop_else_clauses.py` — for/else and while/else for searches, prime tests and nested-loop breaks.
- `08_ternary_expressions.py` — Conditional expressions, nested ternaries, FizzBuzz in a comprehension and function selection.
- `09_walrus_operator.py` — Assignment expressions in if/while conditions, comprehensions and regex matching.
- `10_match_statement_basics.py` — match/case with literals, alternatives, guards, sequence and star patterns.
- `11_match_mappings_classes.py` — Structural pattern matching on dict events and dataclass instances.
- `12_fizzbuzz_variants.py` — Four FizzBuzz implementations (if, concat, rule table, match) verified to agree.
- `13_functions_defaults_kwargs.py` — Default, positional-only, keyword-only, *args and **kwargs parameters and the mutable-default pitfall.
- `14_scope_and_closures.py` — global, nonlocal, closures with independent state and late-binding lambdas.
- `15_number_guessing_simulation.py` — Binary-search guessing game against fixed secrets with worst/average-case stats.
- `16_boolean_logic.py` — Truth tables, short-circuit evaluation, all/any, bools as ints and De Morgan's laws.
- `17_simple_bank_account.py` — A bank account class with a custom exception, validation and transaction history.
- `18_nested_loops_patterns.py` — Triangles, pyramids, squares, diamonds, checkerboards and Pascal's triangle from nested loops.
- `19_tuple_unpacking.py` — Starred, nested and loop unpacking, multiple return values and splatting into calls.
- `20_menu_state_machine.py` — A vending-machine state machine driven by an Enum and match on (state, event) tuples.

## 02_strings/ — Strings (20 programs)

- `01_string_slicing.py` — Positive, negative and stepped slicing, named slice objects, rotation and palindromes.
- `02_case_methods.py` — upper/lower/title/capitalize/swapcase/casefold, case checks and a smart title-caser.
- `03_split_and_join.py` — split, rsplit, splitlines and join for CSV, paths, key=value configs and case conversion.
- `04_strip_and_padding.py` — strip variants, removeprefix/removesuffix, ljust/rjust/center/zfill and expandtabs in a price list.
- `05_find_and_replace.py` — find, rfind, index, count, replace, startswith/endswith with tuples.
- `06_partition_and_parsing.py` — Parsing headers, emails and URLs with partition and rpartition.
- `07_format_specs.py` — The format mini-language: alignment, fill, sign, grouping, bases, percent, nested specs and str.format.
- `08_string_checks.py` — A table of is* predicates across sample strings and a password strength checker.
- `09_encoding_bytes.py` — UTF-8/UTF-16/ASCII encoding, error handlers, code points, bytes and bytearray.
- `10_caesar_cipher.py` — Caesar cipher with str.maketrans/translate, ROT13 and frequency-based cracking.
- `11_word_frequency.py` — Word counting with punctuation stripping, Counter and grouping by length.
- `12_text_wrapping.py` — textwrap fill/wrap/shorten/dedent/indent and a custom full-justification function.
- `13_template_strings.py` — string.Template substitution, custom delimiters, string constants and Formatter.parse.
- `14_regex_basics.py` — Parsing a log with re: findall, named groups, sub with callbacks, split and fullmatch.
- `15_string_building.py` — Building strings with join, repetition and literal concatenation, a table, and run-length encoding.
- `16_anagrams_and_palindromes.py` — Grouping anagrams by sorted key and finding palindromes including the longest substring.
- `17_string_comparison_sorting.py` — Lexicographic, case-insensitive, natural and version sorting plus common prefixes.
- `18_multiline_and_raw_strings.py` — Triple-quoted, raw, escaped, named-Unicode and multi-line f-string literals and docstrings.
- `19_string_immutability.py` — Immutability errors and idioms for building modified copies of strings.
- `20_report_formatter.py` — A formatted regional sales report combining alignment, grouping, percentages and bars.

## 03_lists/ — Lists (20 programs)

- `01_list_basics.py` — Creating, indexing, appending, inserting, popping, removing and searching list elements.
- `02_slicing_and_steps.py` — Stepped/negative slices, slice assignment and deletion, chunks and windows.
- `03_list_comprehensions.py` — Comprehensions with filters, nesting, transposition, Pythagorean triples and primes.
- `04_sorting_with_keys.py` — sorted/sort with key functions, itemgetter/attrgetter, multi-key and stable sorting.
- `05_enumerate_and_zip.py` — enumerate, zip, strict zip, zip_longest, unzipping and pairwise differences.
- `06_nested_lists_matrix.py` — Matrix add, multiply, transpose, identity and rotation with nested lists, plus the aliasing pitfall.
- `07_copying_lists.py` — Aliasing vs shallow vs deep copies, including self-referential lists.
- `08_stack_and_queue.py` — Bracket matching and RPN evaluation with list stacks; round-robin scheduling with deque.
- `09_in_place_operations.py` — +=, *=, reverse, sort, slice replacement and safe deletion while iterating.
- `10_searching_with_bisect.py` — Manual binary search and the bisect module for insertion, grading and range counts.
- `11_list_aggregations.py` — sum/min/max/any/all, statistics, ranking, running max and moving averages.
- `12_flatten_and_chunk.py` — Recursive and generator flattening, chain, chunking with islice and batched.
- `13_list_of_records.py` — Querying, sorting, grouping and annotating a list of book dictionaries.
- `14_list_unpacking_and_star.py` — Starred unpacking, list splatting into calls and print, swapping and rotation.
- `15_two_pointer_algorithms.py` — Two-sum, dedupe, merge, container-with-most-water and in-place reversal with two pointers.
- `16_sorting_algorithms.py` — Insertion, selection, merge and quick sort checked against sorted() on LCG-generated data.
- `17_list_equality_and_membership.py` — List equality, lexicographic ordering, membership, sublists and NaN identity.
- `18_heapq_priority.py` — heapq for heap sort, priority queues, merging sorted lists and a running median.
- `19_itertools_on_lists.py` — accumulate, groupby, permutations, combinations, product, pairwise, compress, takewhile.
- `20_inventory_manager.py` — An inventory of tuples processed with order fulfillment, filtering and value sorting.

## 04_dicts/ — Dictionaries (20 programs)

- `01_dict_basics.py` — Creating, accessing, adding and deleting keys, constructors, fromkeys and hashable keys.
- `02_get_setdefault_pop.py` — get, setdefault, pop and popitem for safe access, grouping and counting.
- `03_iterating_dicts.py` — Iterating keys/values/items, sorted iteration, live views and key-view set operations.
- `04_dict_comprehensions.py` — Dict comprehensions for transforming, filtering, inverting and nesting data.
- `05_counter_usage.py` — Counter tallies, most_common, arithmetic, update/subtract and anagram checks.
- `06_defaultdict_grouping.py` — defaultdict with float, set, list, int and nested factories for grouping and graphs.
- `07_ordered_dict.py` — OrderedDict move_to_end/popitem, order-sensitive equality and an LRU cache.
- `08_nested_dicts.py` — Navigating and aggregating a nested org chart with dotted-path lookup and a recursive walker.
- `09_merging_dicts.py` — Merging with |, |=, update, ** unpacking, ChainMap and a recursive deep merge.
- `10_inverting_and_mapping.py` — Inverting dicts with and without collisions, Morse translation and joining mappings.
- `11_word_index.py` — An inverted index over documents with AND/OR queries.
- `12_json_round_trip.py` — json.dumps/loads with indentation, sorting, separators, errors and custom defaults.
- `13_dict_as_dispatch.py` — Command and operator dispatch tables mapping names and types to functions.
- `14_memoization_cache.py` — Dict memoization, lru_cache, cache, and DP tables keyed by tuples.
- `15_dict_views_and_sets.py` — Diffing two configs with key and item view set algebra.
- `16_phonebook_app.py` — A phonebook class supporting add, update, search, tags and removal.
- `17_graph_bfs_with_dicts.py` — BFS, DFS, path reconstruction and Dijkstra on dict-based graphs.
- `18_typed_dict_records.py` — TypedDict with NotRequired fields and runtime schema validation of records.
- `19_sparse_matrix.py` — A sparse matrix keyed by (row, col) tuples with addition and multiplication.
- `20_student_gradebook.py` — A nested-dict gradebook with averages, best per subject, missing work and letter grades.

## 05_numbers_math/ — Numbers and math (20 programs)

- `01_integer_division_modulo.py` — Floor division, modulo and divmod with negatives, time breakdowns and clock arithmetic.
- `02_big_integers.py` — Arbitrary-precision factorials, powers, Fibonacci, gcd/isqrt, comb and byte conversion.
- `03_float_precision.py` — Float representation, fsum, inf/nan, epsilon, ulp and isclose tolerances.
- `04_rounding_modes.py` — round() banker's rounding, floor/ceil/trunc and Decimal rounding modes compared.
- `05_pow_and_modular_arithmetic.py` — Three-argument pow, modular inverses, Miller-Rabin primality and toy RSA.
- `06_math_module_tour.py` — Constants, roots, logs, trig, combinatorics and special functions from math.
- `07_fractions_exact.py` — Exact Fraction arithmetic, limit_denominator, harmonic numbers and Egyptian fractions.
- `08_decimal_money.py` — Decimal money math with quantize, bill splitting, compound interest and local contexts.
- `09_number_bases.py` — bin/oct/hex, int(x, base), custom base conversion, bit counts and Roman numerals.
- `10_bitwise_operations.py` — Bitwise operators, permission flags, bit tricks, subset masks and Gray codes.
- `11_primes_and_factors.py` — Sieve of Eratosthenes, factorization, divisor counts, totients and perfect numbers.
- `12_statistics_summary.py` — statistics module: averages, spread, quantiles, regression, NormalDist and a histogram.
- `13_number_formatting.py` — Number formatting with separators, padding, percentages, human-readable sizes and ordinals.
- `14_complex_numbers.py` — Complex arithmetic, polar form, roots of unity, quadratic roots and a Mandelbrot test.
- `15_numeric_algorithms.py` — Newton's method, bisection, Simpson and trapezoid integration, and series for e and pi.
- `16_gcd_lcm_euclid.py` — Euclid's algorithm, extended GCD, LCM folding, fraction simplification and Diophantine solving.
- `17_sequences_and_series.py` — Generator-based sequences (Fibonacci, triangular, Collatz, look-and-say) and series sums.
- `18_vector_class_operators.py` — A 2D Vector class with arithmetic dunders, total_ordering, dot products and angles.
- `19_unit_conversion_enum.py` — Length and weight conversions using Enum members with float and Decimal factors.
- `20_loan_amortization.py` — A Decimal loan amortization schedule with payments compared across terms.

## 06_functions/ — Functions (20 programs)

- `01_default_arguments.py` — Default argument values, including the mutable-default pitfall and the None idiom.
- `02_keyword_only_args.py` — Keyword-only parameters enforced with a bare star in the signature.
- `03_positional_only_args.py` — Positional-only parameters using the slash marker, mixed with other kinds.
- `04_star_args.py` — Variadic positional arguments with *args for aggregation helpers.
- `05_kwargs.py` — Variadic keyword arguments with **kwargs for configuration merging.
- `06_unpacking_in_calls.py` — Argument unpacking with * and ** at call sites, including multiple unpackings.
- `07_closures_counter.py` — Closures that capture state: counters, accumulators, and late-binding behavior.
- `08_nonlocal_global.py` — The global and nonlocal statements and how Python resolves names (LEGB).
- `09_recursion_basics.py` — Classic recursive functions: factorial, gcd, power, palindromes, and binary search.
- `10_recursion_tree.py` — Recursion over nested data: flattening, depth, tree sums, permutations, and Hanoi.
- `11_memoization.py` — Memoizing recursive functions with a hand-written decorator and functools caches.
- `12_lambdas_sorting.py` — Lambdas as sort keys, with map/filter/reduce and operator helpers.
- `13_docstrings_annotations.py` — Function docstrings, type annotations, and introspecting them at runtime.
- `14_decorators.py` — Function decorators: plain, parameterized, stacked, and with functools.wraps.
- `15_higher_order_functions.py` — Higher-order functions: composing, piping, and returning functions.
- `16_partial_functions.py` — Partial application with functools.partial and partialmethod.
- `17_single_dispatch.py` — Single-dispatch generic functions with functools.singledispatch.
- `18_function_attributes.py` — Functions as first-class objects: attributes, registries, and dispatch tables.
- `19_validator_factories.py` — Functions that build other functions: a tiny validation library using closures.
- `20_argument_binding.py` — A parameter list mixing every kind of argument, exercised with many call shapes.

## 07_classes_objects/ — Classes and objects (20 programs)

- `01_basic_class.py` — A simple BankAccount class with __init__, instance methods, and state changes.
- `02_repr_and_str.py` — __repr__ versus __str__ and how print, f-strings, and containers use them.
- `03_properties.py` — Managed attributes with @property, setters, deleters, and computed values.
- `04_classmethods_staticmethods.py` — Alternative constructors with @classmethod and utility helpers with @staticmethod.
- `05_class_attributes.py` — Class attributes versus instance attributes, shared counters, and shadowing.
- `06_equality_and_hashing.py` — Defining __eq__ and __hash__ so objects work as set members and dict keys.
- `07_ordering_total_ordering.py` — Rich comparisons with __lt__ and friends, completed by functools.total_ordering.
- `08_vector_operators.py` — Operator overloading on a 2D vector: arithmetic, unary, reflected, and in-place ops.
- `09_slots.py` — Memory-lean classes with __slots__ and the restrictions they impose.
- `10_container_protocol.py` — Making a class behave like a container: __len__, __getitem__, __contains__, __iter__.
- `11_callable_objects.py` — Instances that act like functions via __call__, keeping state between calls.
- `12_fraction_class.py` — A rational-number class implementing arithmetic, comparison, and normalization.
- `13_matrix_class.py` — A small Matrix class with indexing, matrix multiplication (@), transpose, and equality.
- `14_class_namespaces.py` — Class bodies as namespaces: nested classes, class-level computation, and __class__.
- `15_getattr_dynamic.py` — Dynamic attribute access with getattr/setattr/hasattr and __getattr__ fallbacks.
- `16_inventory_system.py` — A small inventory system combining several cooperating classes.
- `17_dataclass_basics.py` — Dataclasses: generated __init__/__repr__/__eq__, defaults, ordering, and frozen instances.
- `18_enum_classes.py` — Enumerations with enum.Enum, auto, IntEnum, Flag, and methods on members.
- `19_linked_list_class.py` — A singly linked list class with append, prepend, reverse, iteration, and indexing.
- `20_object_lifecycle.py` — Instance creation with __new__, singletons, interning caches, and copying objects.

## 08_inheritance/ — Inheritance (20 programs)

- `01_simple_inheritance.py` — Single inheritance: a base Animal class and subclasses overriding behavior.
- `02_super_init_chain.py` — Chaining constructors with super() through a three-level hierarchy.
- `03_method_overriding.py` — Overriding methods while extending the parent implementation via super().
- `04_multiple_inheritance_mro.py` — Multiple inheritance, the diamond problem, and C3 method resolution order.
- `05_abstract_base_classes.py` — Abstract base classes with abc.ABC and @abstractmethod enforcing an interface.
- `06_abstract_properties.py` — Abstract properties and classmethods in an ABC for a plugin-style hierarchy.
- `07_mixins.py` — Mixin classes that add reusable behavior (serialization, comparison, repr) to models.
- `08_isinstance_issubclass.py` — Type checks with isinstance and issubclass, including tuples of types and ABCs.
- `09_polymorphism_payroll.py` — Polymorphism in a payroll system where each employee type computes pay differently.
- `10_duck_typing.py` — Duck typing versus inheritance: unrelated classes used through a shared protocol.
- `11_super_with_kwargs.py` — Cooperative multiple inheritance where every __init__ passes **kwargs along super().
- `12_overriding_dunders.py` — Subclassing built-in types (dict, list, str) and overriding their special methods.
- `13_template_method.py` — The template method pattern: a base class algorithm with overridable hook steps.
- `14_expression_tree.py` — A polymorphic expression tree where each node subclass implements evaluate and str.
- `15_abc_register_virtual.py` — Virtual subclasses via ABC.register and structural checks with __subclasshook__.
- `16_class_hierarchy_introspection.py` — Walking a class hierarchy with __subclasses__, __bases__, and __init_subclass__.
- `17_composition_vs_inheritance.py` — Composition versus inheritance: a Stack built both ways and their differences.
- `18_state_machine_polymorphism.py` — Polymorphic state machine: traffic-light states as subclasses that return the next state.
- `19_super_in_classmethods.py` — Using super() inside classmethods and properties across an inheritance chain.
- `20_bank_account_hierarchy.py` — A bank account hierarchy with overridden withdrawal rules and interest policies.

## 09_iterators_generators/ — Iterators and generators (20 programs)

- `01_iterator_protocol.py` — Implementing the iterator protocol by hand with __iter__ and __next__.
- `02_simple_generators.py` — Generator functions with yield: lazy sequences and resumable state.
- `03_yield_from.py` — Delegating to sub-generators with yield from, including return values.
- `04_generator_expressions.py` — Generator expressions versus list comprehensions, and consuming them lazily.
- `05_send_coroutines.py` — Generator-based coroutines that receive values with send() and keep running state.
- `06_itertools_infinite.py` — Infinite iterators from itertools: count, cycle, repeat, bounded with islice.
- `07_itertools_combinatorics.py` — Combinatoric iterators: product, permutations, combinations, and with replacement.
- `08_itertools_chain_groupby.py` — Combining and grouping iterables with chain, chain.from_iterable, and groupby.
- `09_itertools_accumulate.py` — Running totals and scans with itertools.accumulate and various binary functions.
- `10_itertools_takewhile_dropwhile.py` — Predicate-driven slicing with takewhile, dropwhile, filterfalse, and compress.
- `11_itertools_zip_longest.py` — Pairing uneven iterables with zip, zip(strict=True), and itertools.zip_longest.
- `12_lazy_pipeline.py` — A lazy data-processing pipeline chained from small generator stages.
- `13_stateful_iterator_class.py` — A peekable iterator wrapper class with lookahead and push-back support.
- `14_tree_traversal_generators.py` — Binary tree traversals (in/pre/post/level order) written as generators.
- `15_generator_close_throw.py` — Controlling generators from outside with throw(), close(), and try/finally cleanup.
- `16_sliding_windows.py` — Sliding windows, pairwise, and batching over iterators using deque and itertools.
- `17_lcg_random_stream.py` — A deterministic pseudo-random number generator implemented as an infinite generator.
- `18_custom_range_class.py` — A float-friendly range class that is iterable, reversible, sized, and indexable.
- `19_word_frequency_stream.py` — Streaming word-frequency analysis with generators, Counter, and heapq.nlargest.
- `20_interleave_merge.py` — Merging sorted streams lazily with heapq.merge and a hand-written round-robin.

## 10_exceptions/ — Exceptions (20 programs)

- `01_try_except_basics.py` — Basic try/except handling of common built-in exceptions.
- `02_else_finally.py` — The else and finally clauses of try statements and their execution order.
- `03_multiple_except_clauses.py` — Handling several exception types with separate clauses, tuples, and ordering.
- `04_custom_exceptions.py` — Custom exception classes carrying extra data and custom messages.
- `05_exception_hierarchy.py` — Designing a custom exception hierarchy and catching at different levels.
- `06_raise_from_chaining.py` — Explicit exception chaining with raise ... from, and suppressing context with from None.
- `07_reraise_and_wrap.py` — Re-raising exceptions with bare raise after logging, and wrapping at layer boundaries.
- `08_context_manager_class.py` — Writing context managers as classes with __enter__ and __exit__.
- `09_contextmanager_decorator.py` — Generator-based context managers built with contextlib.contextmanager.
- `10_suppress_and_exitstack.py` — Contextlib helpers: suppress, ExitStack, nullcontext, and closing.
- `11_assertions.py` — Assertions for internal invariants and how AssertionError reports failures.
- `12_exception_attributes.py` — Inspecting exception objects: args, str/repr, notes added with add_note, and related attributes.
- `13_validation_pipeline.py` — Collecting validation errors across many records instead of failing on the first.
- `14_retry_with_backoff.py` — A retry decorator that catches selected exceptions and computes a backoff schedule.
- `15_cleanup_order.py` — Tracing the exact order of try/except/else/finally across nested calls and exceptions.
- `16_eafp_vs_lbyl.py` — EAFP (try first) versus LBYL (check first) styles applied to the same tasks.
- `17_safe_calculator.py` — A small expression calculator that reports errors with custom exception types.
- `18_exceptions_in_generators.py` — How exceptions interact with generators, comprehensions, and StopIteration.
- `19_resource_pool.py` — A connection pool that uses context managers to guarantee resources are returned.
- `20_error_reporting_summary.py` — Running a batch of jobs, isolating failures, and summarizing errors by type.

## 11_sets_tuples/ — Sets and tuples (20 programs)

- `01_set_basics.py` — Creates sets, adds and removes members, and checks membership.
- `02_set_operators.py` — Demonstrates union, intersection, difference and symmetric difference with operators and methods.
- `03_set_inplace_ops.py` — Uses augmented assignment and update methods to mutate sets in place.
- `04_subset_superset.py` — Checks subset, superset and disjointness relations between permission sets.
- `05_frozenset_keys.py` — Uses frozensets as dictionary keys and set members to model unordered pairs.
- `06_set_comprehensions.py` — Builds sets with comprehensions including conditions and nested loops.
- `07_dedupe_preserve_order.py` — Removes duplicates while preserving first-seen order using a seen-set.
- `08_tuple_basics.py` — Explores tuple creation, indexing, slicing, concatenation and immutability.
- `09_tuple_unpacking.py` — Shows tuple unpacking in assignments, loops, swaps and nested patterns.
- `10_starred_unpacking.py` — Uses starred expressions to capture heads, tails and middles of sequences.
- `11_namedtuple_basics.py` — Defines a collections.namedtuple and uses field access, _replace, _asdict and _make.
- `12_typing_namedtuple.py` — Defines typed NamedTuple classes with defaults, methods and properties.
- `13_tuples_as_dict_keys.py` — Uses tuples as composite dictionary keys for a sparse grid and lookup tables.
- `14_zip_and_enumerate.py` — Combines zip, enumerate and tuple sequences for parallel iteration.
- `15_tuple_sorting.py` — Sorts lists of tuples lexicographically and by computed keys using operator.itemgetter.
- `16_set_word_analysis.py` — Analyses vocabulary overlap between texts using sets and Jaccard similarity.
- `17_graph_with_sets.py` — Represents an undirected graph with adjacency sets and finds common friends and components.
- `18_tuple_records.py` — Processes immutable tuple records with grouping, aggregation and min/max queries.
- `19_namedtuple_geometry.py` — Builds geometry helpers on namedtuple subclasses for points, segments and polygons.
- `20_set_state_machine.py` — Computes epsilon-closures and simulates an NFA using sets of frozen states.

## 12_recursion/ — Recursion (20 programs)

- `01_factorial.py` — Computes factorials recursively, iteratively and with math.factorial and compares results.
- `02_fibonacci_memo.py` — Contrasts naive, lru_cache, functools.cache and dict-memoised Fibonacci implementations.
- `03_towers_of_hanoi.py` — Solves the Towers of Hanoi recursively, listing moves and tracking peg states.
- `04_permutations.py` — Generates permutations recursively, with and without duplicates, and checks against itertools.
- `05_subsets_powerset.py` — Enumerates subsets recursively, finds subset sums and generates combinations by backtracking.
- `06_flood_fill.py` — Applies recursive flood fill to a character grid to count and label regions.
- `07_ackermann.py` — Evaluates the Ackermann function for small inputs with memoisation and call counting.
- `08_nested_structure_walk.py` — Recursively walks nested dicts and lists to flatten paths, count values and find keys.
- `09_mutual_recursion.py` — Uses mutually recursive functions for parity, Hofstadter sequences and a tiny grammar.
- `10_binary_strings.py` — Generates binary strings, Gray codes and strings without consecutive ones recursively.
- `11_recursive_tree_class.py` — Builds a recursive expression tree with dataclasses and evaluates, prints and simplifies it.
- `12_gcd_and_power.py` — Implements Euclid's GCD, extended GCD and fast exponentiation recursively.
- `13_n_queens.py` — Solves the N-Queens puzzle by recursive backtracking and prints a board.
- `14_merge_recursive_lists.py` — Recursively flattens, reverses, sums and merges nested Python lists.
- `15_palindromes_strings.py` — Uses recursion for palindromes, string reversal, edit distance and partitioning.
- `16_coin_change.py` — Counts coin change combinations and finds minimum coins with memoised recursion.
- `17_tree_traversals.py` — Performs recursive preorder, inorder, postorder traversals and measures a binary tree.
- `18_sudoku_solver.py` — Solves a 4x4 and a 9x9 Sudoku puzzle using recursive backtracking.
- `19_catalan_structures.py` — Generates balanced parentheses and counts binary trees, verifying Catalan numbers.
- `20_recursive_descent_calc.py` — Implements a recursive-descent arithmetic parser and evaluator with precedence and parentheses.

## 13_sorting/ — Sorting (20 programs)

- `01_bubble_sort.py` — Implements bubble sort with early exit and counts comparisons and swaps.
- `02_insertion_sort.py` — Implements insertion sort in place, a binary-insertion variant and sorting by key.
- `03_selection_sort.py` — Implements selection sort and a double-ended variant, tracking minimum selections.
- `04_merge_sort.py` — Implements top-down and bottom-up merge sort and counts inversions during merging.
- `05_quick_sort.py` — Implements quicksort with Lomuto and Hoare partitions plus a three-way functional version.
- `06_heap_sort.py` — Implements in-place heap sort with sift-down and compares with heapq-based sorting.
- `07_counting_sort.py` — Implements a stable counting sort for integers and for records keyed by small integers.
- `08_radix_sort.py` — Implements LSD radix sort for integers and MSD-style sorting for fixed-length strings.
- `09_shell_sort.py` — Implements Shell sort with several gap sequences and compares the number of moves.
- `10_bucket_sort.py` — Distributes floats and scores into buckets, sorts each bucket and concatenates them.
- `11_timsort_ish.py` — Implements a simplified Timsort detecting runs, extending with insertion sort and merging.
- `12_sorted_key_reverse.py` — Uses sorted() and list.sort() with key functions, reverse flags and operator helpers.
- `13_cmp_to_key.py` — Uses functools.cmp_to_key with custom comparators for largest-number and versions.
- `14_stable_multikey_sort.py` — Performs multi-key sorts by chaining stable sorts and by composite tuple keys.
- `15_sort_dataclasses_order.py` — Sorts dataclass instances using order=True, field(compare=False) and total_ordering.
- `16_sort_strings_natural.py` — Sorts filenames naturally using regex-split keys and handles case and accents.
- `17_sort_by_frequency.py` — Sorts elements by frequency using Counter, with ties broken by value or first occurrence.
- `18_odd_even_and_gnome.py` — Implements gnome sort, odd-even transposition sort and comb sort with step traces.
- `19_sort_matrix_and_intervals.py` — Sorts matrix rows and columns and merges overlapping intervals after sorting.
- `20_sorting_benchmark_counts.py` — Compares comparison counts of several sorts on the same data using a counting wrapper class.

## 14_searching/ — Searching (20 programs)

- `01_linear_search.py` — Implements linear search variants including sentinel search, find-all and predicate search.
- `02_binary_search.py` — Implements iterative and recursive binary search plus lower and upper bound variants.
- `03_bisect_module.py` — Uses the bisect module for insertion points, grade lookup, sorted inserts and range counts.
- `04_interpolation_search.py` — Implements interpolation search on uniform data and compares probes with binary search.
- `05_two_pointers.py` — Solves pair-sum, three-sum, deduplication and container problems with two pointers.
- `06_sliding_window.py` — Applies fixed and variable sliding windows for max sums, longest substrings and anagrams.
- `07_ternary_search.py` — Uses ternary search to find extrema of unimodal functions over integers and reals.
- `08_rotated_array_search.py` — Finds a target and the rotation pivot in rotated sorted arrays with modified binary search.
- `09_bfs_grid.py` — Finds shortest paths through a maze grid with breadth-first search and reconstructs the path.
- `10_dfs_grid.py` — Uses iterative and recursive depth-first search to count islands and find the largest one.
- `11_kth_element.py` — Finds the k-th smallest element with sorting, heapq and quickselect, and medians of streams.
- `12_search_2d_matrix.py` — Searches row/column-sorted matrices with staircase search and flattened binary search.
- `13_string_search.py` — Implements naive, KMP and Boyer-Moore-Horspool substring search and compares with str.find and re.
- `14_exponential_search.py` — Implements exponential and jump search for sorted arrays and unbounded sequences.
- `15_search_with_dict_index.py` — Builds inverted and prefix indexes with dicts for fast keyword and prefix lookups.
- `16_peak_and_boundary.py` — Uses binary search on answers to find peaks, first bad versions and minimum capacities.
- `17_word_ladder_bfs.py` — Solves word ladder puzzles with BFS over implicit word graphs using wildcard buckets.
- `18_backtracking_word_search.py` — Searches a letter grid for words with DFS backtracking and a prefix set for pruning.
- `19_dijkstra_search.py` — Finds weighted shortest paths with Dijkstra's algorithm using heapq on a city road graph.
- `20_astar_search.py` — Finds a path on a weighted grid using A* search with a Manhattan heuristic.

## 15_data_structures/ — Data structures (20 programs)

- `01_stack_class.py` — Implements a stack class and uses it for bracket matching and postfix evaluation.
- `02_deque_queue.py` — Uses collections.deque as a FIFO queue, a bounded history buffer and for rotations.
- `03_singly_linked_list.py` — Implements a singly linked list with append, insert, delete, reverse and iteration.
- `04_doubly_linked_list.py` — Implements a doubly linked list with sentinel nodes supporting both-end operations.
- `05_binary_search_tree.py` — Implements a binary search tree with insert, search, delete, traversal and height.
- `06_heapq_priority_queue.py` — Builds a priority task queue on heapq with stable ordering, updates and lazy deletion.
- `07_trie.py` — Implements a trie with insert, search, prefix listing, counts and deletion.
- `08_union_find.py` — Implements union-find with path compression and union by rank for components and Kruskal.
- `09_lru_cache_ordereddict.py` — Implements an LRU cache with OrderedDict and compares it to functools.lru_cache.
- `10_hash_map_impl.py` — Implements a hash map with separate chaining, resizing and dict-like dunder methods.
- `11_circular_buffer.py` — Implements a fixed-size circular ring buffer with overwrite policy and moving averages.
- `12_segment_tree.py` — Builds a segment tree for range-sum and range-min queries with point updates.
- `13_min_stack_and_queue_two_stacks.py` — Implements a min-tracking stack and a queue built from two stacks.
- `14_graph_adjacency.py` — Implements a directed graph class with adjacency lists, topological sort and cycle detection.
- `15_sparse_matrix.py` — Implements a dictionary-of-keys sparse matrix with addition, multiplication and transpose.
- `16_bloom_and_bitset.py` — Implements a bitset on Python ints and a small Bloom filter with deterministic hashes.
- `17_ordered_set_skiplist.py` — Implements a deterministic skip list supporting insert, search, delete and range queries.
- `18_dataclass_inventory.py` — Models an inventory with dataclasses, defaultdict indexes and Counter summaries.
- `19_abstract_containers.py` — Defines an abstract collection interface with abc and implements array- and linked-backed versions.
- `20_fenwick_tree.py` — Implements a Fenwick (binary indexed) tree for prefix sums, range sums and inversion counting.

## 16_graphs/ — Graphs (20 programs)

- `01_adjacency_representations.py` — Builds adjacency-list and adjacency-matrix views of one graph and checks degree sums.
- `02_bfs_shortest_path.py` — Breadth-first search for unweighted shortest paths and distance levels with deque.
- `03_dfs_recursive_iterative.py` — Recursive and explicit-stack depth-first search plus connected components.
- `04_dijkstra_heapq.py` — Dijkstra's shortest paths over a road network using heapq, with route reconstruction.
- `05_bellman_ford.py` — Bellman-Ford with negative edges and negative-cycle detection using a NamedTuple edge type.
- `06_floyd_warshall.py` — Floyd-Warshall all-pairs shortest paths with path reconstruction, eccentricity and graph centre.
- `07_topological_sort.py` — Topological sort of a build dependency graph via Kahn's algorithm and DFS, with build stages and cycle errors.
- `08_kruskal_union_find.py` — Kruskal's minimum spanning tree using a union-find class with path compression and union by rank.
- `09_prim_mst.py` — Prim's MST with a lazy heap and a dense O(V^2) matrix variant on Manhattan-distance points.
- `10_tarjan_scc.py` — Tarjan's strongly connected components with nonlocal state and the condensation DAG.
- `11_kosaraju_scc.py` — Kosaraju's two-pass SCC algorithm with an iterator-based iterative DFS on a call graph.
- `12_bipartite_check.py` — BFS two-colouring to test bipartiteness and extract an odd cycle when it fails.
- `13_cycle_detection.py` — Cycle detection in directed graphs (three-colour DFS with an Enum) and undirected graphs (union-find).
- `14_bridges_articulation.py` — Finds bridges and articulation points of a network using low-link values.
- `15_astar_grid.py` — A* search on a character maze with a Manhattan heuristic and rendered path.
- `16_max_flow_edmonds_karp.py` — Edmonds-Karp maximum flow with augmenting paths and min-cut extraction.
- `17_eulerian_path.py` — Hierholzer's algorithm for Eulerian paths, applied to flight itineraries and domino circuits.
- `18_word_ladder.py` — Word ladder shortest transformations by BFS over wildcard buckets.
- `19_grid_islands.py` — Counts islands on a grid map, measures area and perimeter, labels them and flood-fills.
- `20_graph_coloring.py` — Greedy and backtracking graph colouring for exam scheduling using a dataclass graph.

## 17_dynamic_programming/ — Dynamic programming (20 programs)

- `01_knapsack_01.py` — 0/1 knapsack with full-table item reconstruction and a 1-D space-optimised version.
- `02_unbounded_knapsack.py` — Unbounded knapsack filling a cargo hold, with Counter-based reconstruction.
- `03_longest_increasing_subsequence.py` — LIS by O(n^2) DP and O(n log n) patience sorting with bisect.
- `04_longest_common_subsequence.py` — LCS table and backtracking, plus a line-based diff built on it.
- `05_edit_distance.py` — Edit distance with an explicit operation script, Enum ops and weighted costs.
- `06_coin_change.py` — Minimum coins, number of ways (tabulated and lru_cache), and a greedy counterexample.
- `07_matrix_chain.py` — Matrix chain multiplication order with optimal parenthesisation.
- `08_rod_cutting.py` — Rod cutting with functools.cache top-down memoisation and bottom-up tabulation.
- `09_word_break.py` — Word break feasibility, counting segmentations, and listing all sentences.
- `10_integer_partitions.py` — Partition counts (all, distinct, odd parts), Euler's pentagonal recurrence, and a generator of partitions.
- `11_grid_paths.py` — Lattice-path counting with obstacles and minimum-cost path with reconstruction.
- `12_longest_palindromic_subsequence.py` — Longest palindromic subsequence, minimum insertions and minimum palindrome cuts.
- `13_egg_drop.py` — Egg drop puzzle via memoised DP, the binomial moves formulation, and a simulated strategy.
- `14_fibonacci_forms.py` — Fibonacci computed naively, with dict memo, lru_cache, tabulation, generator and fast doubling.
- `15_subset_sum_partition.py` — Subset sum with integer bitsets, balanced partition, and +/- target-sum counting.
- `16_max_subarray.py` — Kadane's algorithm in 1-D, circular arrays, and the maximum-sum rectangle in 2-D.
- `17_stock_state_machine.py` — State-machine DP for house robber and stock trading with cooldown, fees and k transactions.
- `18_catalan_structures.py` — Catalan numbers via DP and enumeration of balanced parentheses and BST shapes.
- `19_common_substring_supersequence.py` — Longest common substring and shortest common supersequence of string pairs.
- `20_tsp_bitmask.py` — Held-Karp bitmask DP for the travelling salesman, checked against brute force.

## 18_number_theory/ — Number theory (20 programs)

- `01_sieve_of_eratosthenes.py` — Sieve of Eratosthenes with bytearray slicing, a segmented sieve, and prime-counting statistics.
- `02_gcd_lcm.py` — Recursive, iterative and binary GCD compared with math.gcd and math.lcm.
- `03_extended_euclid.py` — Extended Euclid, modular inverses, and linear Diophantine equations.
- `04_chinese_remainder.py` — Chinese Remainder Theorem for coprime and non-coprime moduli, including secret sharing.
- `05_euler_totient.py` — Euler's totient by factorisation and by sieve, with Euler's theorem checks.
- `06_fast_exponentiation.py` — Square-and-multiply, three-argument pow, and matrix powers for huge Fibonacci indices.
- `07_miller_rabin.py` — Deterministic Miller-Rabin for 64-bit integers, with Carmichael numbers and strong pseudoprimes.
- `08_perfect_amicable.py` — Perfect, abundant, deficient and amicable numbers from a divisor-sum sieve.
- `09_digit_problems.py` — Digit sums, digital roots, Armstrong, happy, Kaprekar, Harshad and reverse-and-add numbers.
- `10_big_factorials.py` — Exact big factorials, trailing zeros, Legendre's formula, binomials and Stirling's approximation.
- `11_big_fibonacci.py` — F(200) exactly, Pisano periods, Fibonacci identities and Zeckendorf representation.
- `12_continued_fractions.py` — Continued fractions of rationals and square roots, convergents with Fraction, and Pell equations.
- `13_pythagorean_triples.py` — Pythagorean triples via Euclid's formula and the Berggren tree using a NamedTuple with properties.
- `14_prime_factorization.py` — Prime factorisation with trial division and Pollard's rho.
- `15_divisor_functions.py` — Divisor functions tau and sigma, highly composite numbers, and multiplicativity checks.
- `16_collatz.py` — Collatz chain lengths with lru_cache, record holders, peaks and a histogram.
- `17_base_conversion.py` — Conversion to any radix, balanced ternary, factoradic permutations and double-base palindromes.
- `18_modint_class.py` — A ModInt class with full operator overloading used for modular combinatorics.
- `19_decimal_expansions.py` — Repeating decimal periods by long division and high-precision constants with decimal.
- `20_goldbach_twin_primes.py` — Goldbach partitions, twin/cousin/sexy primes and primes in arithmetic progression.

## 19_string_algorithms/ — String algorithms (20 programs)

- `01_kmp_search.py` — Knuth-Morris-Pratt search with its failure table and smallest-period detection.
- `02_z_algorithm.py` — Z-arrays for pattern matching, borders and counting distinct substrings.
- `03_rabin_karp.py` — Rabin-Karp rolling hash search, multi-pattern search and longest duplicate substring.
- `04_manacher.py` — Manacher's linear-time longest palindromic substring checked against expand-around-centre.
- `05_suffix_array.py` — Suffix arrays by sorting and prefix doubling, the Kasai LCP array and bisect-based queries.
- `06_longest_common_prefix.py` — Longest common prefix computed five different ways, including reduce and zip/takewhile.
- `07_anagram_grouping.py` — Anagram families by sorted key and letter counts, plus sliding-window anagram search.
- `08_run_length_encoding.py` — Run-length encoding with groupby and regex decoding, and the look-and-say sequence.
- `09_caesar_vigenere.py` — Caesar and Vigenere ciphers with str.maketrans and chi-squared cracking of Caesar.
- `10_huffman_coding.py` — Huffman coding with an ordered dataclass node, heapq tree building, encode and decode.
- `11_levenshtein_spellcheck.py` — Levenshtein and Damerau distances driving a tiny spelling corrector.
- `12_palindromes.py` — Sentence palindromes, palindromic permutations, palindrome pairs and next palindrome.
- `13_balanced_brackets.py` — Bracket balancing with error positions, minimum fixes and generation of balanced strings.
- `14_base64_by_hand.py` — Base64 encoding and decoding implemented by hand with bit manipulation.
- `15_trie_autocomplete.py` — A prefix trie with ranked autocomplete, wildcard matching, deletion and dunder methods.
- `16_boyer_moore_horspool.py` — Boyer-Moore-Horspool search compared with naive search by comparison counts.
- `17_aho_corasick.py` — Aho-Corasick automaton for multi-keyword search used as a censoring filter.
- `18_string_rotations.py` — Rotation tests, Booth's least rotation, Lyndon factorisation and binary necklaces.
- `19_burrows_wheeler.py` — Burrows-Wheeler transform and inverse followed by move-to-front coding.
- `20_lzw_compression.py` — LZW compression and decompression with a growing dictionary and bit-width accounting.

## 20_text_processing/ — Text processing (20 programs)

- `01_word_frequency.py` — Word frequency analysis with Counter, stop words, hapax legomena and bigrams.
- `02_regex_tokenizer.py` — A named-group regex tokenizer for a small language with line/column tracking.
- `03_csv_by_hand.py` — Quote-aware CSV parsing from an in-program string, aggregation and re-serialisation.
- `04_string_template.py` — string.Template substitution, safe_substitute, custom delimiters and patterns for mail merge.
- `05_textwrap_tools.py` — textwrap wrap, fill, shorten, dedent, indent and a TextWrapper for bullet lists.
- `06_justify_text.py` — Left, right, centre and full justification of paragraphs with an alignment Enum.
- `07_markdown_to_text.py` — Converts a small Markdown document to plain text, including links and code blocks.
- `08_log_parsing.py` — Parses web-server access logs with a verbose regex and summarises traffic.
- `09_json_roundtrip.py` — json.dumps/json.loads round trips with a custom encoder and object hook for dataclasses, Enums and Decimals.
- `10_report_table.py` — Renders sales data as aligned text tables with totals, subtotals and format specs.
- `11_readability_stats.py` — Sentence splitting, syllable counting and Flesch readability scores.
- `12_ini_config_parser.py` — A hand-written INI parser with sections, continuations, interpolation and typed values.
- `13_ngram_model.py` — Word and character n-grams, a deterministic bigram text generator and Jaccard similarity.
- `14_case_conversion_slugify.py` — Converts identifiers between camel, snake, kebab and Pascal case, and generates URL slugs.
- `15_keyword_in_context.py` — Keyword-in-context concordance and collocation counts.
- `16_extract_contacts.py` — Extracts and normalises emails, URLs, phone numbers, dates and hashtags with regex.
- `17_number_to_words.py` — Spells out numbers in English, ordinals and cheque-style amounts.
- `18_letter_histogram.py` — Letter-frequency histograms as horizontal and vertical bar charts, plus a pangram checker.
- `19_query_string_parser.py` — Parses and builds URLs and query strings by hand with percent-encoding.
- `20_inverted_index_search.py` — An inverted index with TF-IDF ranking, boolean queries and phrase search.

## 21_simulations/ — Simulations (20 programs)

- `01_bank_accounts.py` — Bank accounts with Decimal balances, transfers, a custom exception and monthly interest.
- `02_vending_machine.py` — Vending machine as an Enum-driven finite state machine processing a stream of events.
- `03_game_of_life.py` — Conway's Game of Life on a set of live cells using Counter, with a glider and a blinker.
- `04_elevator.py` — Single elevator serving timed floor requests with the SCAN algorithm.
- `05_inventory.py` — Warehouse inventory with FIFO cost lots, reorder points and backorders.
- `06_bank_queue_lcg.py` — Discrete-event multi-teller queue simulation driven by a hand-written LCG and a heap.
- `07_traffic_light.py` — Intersection traffic light controller cycling phases with queued cars on two roads.
- `08_rule30_automaton.py` — Elementary cellular automaton Rule 30 and its center column as a bit generator.
- `09_rule110_automaton.py` — Rule 110 evolution plus density and period comparison of several elementary rules.
- `10_projectile_physics.py` — Projectile motion with and without air drag using time-stepped integration.
- `11_round_robin_tournament.py` — Circle-method round-robin schedule, deterministic results and a standings table.
- `12_library_system.py` — Library lending with holds queues, due dates and overdue fines.
- `13_parking_lot.py` — Parking lot with sized spots allocated via heaps, IntEnum sizes and hourly billing.
- `14_predator_prey.py` — Lotka-Volterra predator-prey model integrated with fourth-order Runge-Kutta.
- `15_epidemic_sir.py` — SIR epidemic model comparing outbreaks with and without interventions.
- `16_random_walk_lcg.py` — 2D lattice random walks with a generator-based LCG, measuring distance and returns.
- `17_dice_game_monte_carlo.py` — Monte Carlo tournament of "Pig" dice strategies using an xorshift generator.
- `18_langtons_ant.py` — Langton's ant and a three-color turmite on an unbounded defaultdict grid.
- `19_cache_simulation.py` — LRU, FIFO and LFU cache policies (ABC subclasses) compared on one access trace.
- `20_cpu_scheduler.py` — FCFS, SJF and round-robin CPU scheduling compared on the same workload.

## 22_functional/ — Functional programming (20 programs)

- `01_map_filter_reduce.py` — Classic map, filter and reduce over a small sales dataset.
- `02_functools_partial.py` — Specializing functions, builtins and callbacks with functools.partial.
- `03_reduce_patterns.py` — Common folds with reduce: gcd/lcm, set algebra, deep lookup, composition, matrix power.
- `04_wraps_decorators.py` — Logging, validation and retry decorators that preserve metadata with functools.wraps.
- `05_singledispatch.py` — A JSON encoder built on singledispatch plus a class using singledispatchmethod.
- `06_cache_memoization.py` — Memoization with functools.cache and lru_cache, including cache statistics.
- `07_operator_module.py` — itemgetter, attrgetter, methodcaller and the arithmetic functions of the operator module.
- `08_function_composition.py` — A Composable wrapper overloading `|` and `@` for left-to-right and mathematical composition.
- `09_currying.py` — A curry decorator supporting partial application in any grouping, plus manual closures.
- `10_immutable_updates.py` — NamedTuple `_replace`, frozensets and persistent-style dictionary updates.
- `11_higher_order_functions.py` — Predicate combinators, flip, twice, iterate and juxt built from functions returning functions.
- `12_generator_pipelines.py` — Lazy generator pipelines parsing and aggregating web-server log lines with regexes.
- `13_closures.py` — Closures with nonlocal state, closure cells, and late-binding pitfalls.
- `14_itertools_functional.py` — accumulate, groupby, starmap, chain, tee, pairwise and friends for data processing.
- `15_sorting_with_keys.py` — Key functions, cmp_to_key, stable multi-pass sorts and natural sort.
- `16_maybe_result_types.py` — Ok/Err result containers with bind/map chaining and structural pattern matching.
- `17_tree_folds.py` — A catamorphism over frozen-dataclass expression trees for evaluation, printing and simplification.
- `18_lazy_streams.py` — Infinite generator streams: incremental prime sieve, Fibonacci, Hamming numbers and combinators.
- `19_total_ordering_partialmethod.py` — total_ordering, partialmethod and cached_property on a Money class.
- `20_text_processing_pipeline.py` — Point-free word-frequency and n-gram analysis built from small composed functions.

## 23_comprehensions_decorators/ — Comprehensions and decorators (20 programs)

- `01_list_comprehensions.py` — List comprehensions for transforming, filtering and generating sequences.
- `02_dict_comprehensions.py` — Dict comprehensions for indexing, inverting, grouping and merging mappings.
- `03_set_comprehensions.py` — Set comprehensions and set algebra for deduplication and membership questions.
- `04_nested_comprehensions.py` — Nested comprehensions for matrix transpose, product, rotation and Pascal's triangle.
- `05_conditional_comprehensions.py` — Comprehensions with filters, chained conditional expressions and the walrus operator.
- `06_generator_expressions.py` — Generator expressions with lazy evaluation, any/all short-circuiting and next() defaults.
- `07_simple_decorators.py` — Basic decorators for tracing recursive calls, counting invocations and preconditions.
- `08_decorators_with_arguments.py` — Decorator factories with arguments, including an optional-arguments decorator.
- `09_class_decorators.py` — Class decorators that add `__repr__`/`__eq__`, comparison methods and singleton behavior.
- `10_stacked_decorators.py` — Stacking decorators and observing their wrap and execution order.
- `11_memoize_decorator.py` — Hand-written memoization decorators with hit statistics and a bounded LRU variant.
- `12_registration_decorators.py` — Registration decorators building a command dispatcher and a prioritized plugin registry.
- `13_property_patterns.py` — @property for validation, computed attributes, deleters, read-only fields and lazy values.
- `14_class_based_decorators.py` — Decorators implemented as classes with `__call__`, including a method-aware one using `__get__`.
- `15_comprehension_scoping.py` — Comprehension scoping rules, walrus leakage, class-body gotchas and late binding.
- `16_method_decorators.py` — staticmethod, classmethod alternate constructors and custom decorators on methods.
- `17_contextmanager_decorators.py` — @contextmanager generators, ContextDecorator classes and contextlib.suppress.
- `18_type_checking_decorator.py` — A decorator enforcing type annotations at call time with optional coercion.
- `19_event_decorators.py` — An event bus whose handlers subscribe via decorators with filters, priorities and once flags.
- `20_gradebook_report.py` — A gradebook report built almost entirely from nested comprehensions.

## 24_dataclasses_dunder/ — Dataclasses and dunder methods (20 programs)

- `01_dataclass_basics.py` — Dataclass defaults, default_factory, generated `__repr__`/`__eq__` and field introspection.
- `02_frozen_dataclass.py` — Frozen dataclasses as hashable value objects updated with dataclasses.replace.
- `03_dataclass_ordering.py` — order=True dataclasses with compare=False fields, sort keys and heap usage.
- `04_post_init_validation.py` — `__post_init__` validation, derived init=False fields and InitVar parameters.
- `05_asdict_serialization.py` — Nested dataclasses converted with asdict/astuple, serialized to JSON and rebuilt.
- `06_enum_basics.py` — Enum with auto values, aliases, @unique, methods, properties and tuple-valued members.
- `07_intenum_and_flag.py` — IntEnum log levels and Flag permission bits combined with bitwise operators.
- `08_vector_dunders.py` — A 2D Vector implementing arithmetic, reflected, in-place, hashing, truthiness and iteration dunders.
- `09_sequence_protocol.py` — A playlist sequence with slicing `__getitem__`, `__setitem__`, `__contains__`, `__reversed__` and more.
- `10_callable_objects.py` — Callable objects via `__call__`: polynomials with Newton's method, running stats and validators.
- `11_format_dunder.py` — Custom `__format__` specs for money, durations and temperatures in f-strings.
- `12_descriptors.py` — Reusable validating descriptors using `__set_name__`, `__get__` and `__set__`.
- `13_getattr_setattr.py` — `__getattr__`, `__setattr__` and `__delattr__` for attribute dicts, change tracking and proxies.
- `14_dynamic_classes.py` — Building a class hierarchy at runtime from a schema with type(), setattr and getattr.
- `15_init_subclass.py` — `__init_subclass__` for automatic registration, required methods and per-class keyword config.
- `16_protocols.py` — Structural typing with typing.Protocol and runtime_checkable versus nominal abc.ABC.
- `17_generic_containers.py` — Generic Stack, BoundedQueue and Registry classes using TypeVar and Generic.
- `18_context_manager_dunders.py` — `__enter__`/`__exit__` for transactions with rollback, nesting and temporary overrides.
- `19_matrix_class.py` — A Matrix class with tuple indexing, `__matmul__`, `__pow__`, transpose and exact determinant.
- `20_rational_numbers.py` — A Rational number class with full arithmetic, reflected operators, conversions and hashing.

## 25_puzzles/ — Puzzles (20 programs)

- `01_n_queens.py` — N-Queens solution counts via set-based and bitmask backtracking, with symmetry reduction.
- `02_sudoku_solver.py` — Sudoku solver using candidate sets and most-constrained-cell backtracking.
- `03_knights_tour.py` — Knight's tours via Warnsdorff's heuristic plus exhaustive tour counts on small boards.
- `04_maze_generate_solve.py` — Perfect maze generation by randomized DFS with an own LCG, solved with BFS.
- `05_word_ladder.py` — Shortest word ladders found by BFS over wildcard buckets.
- `06_eight_puzzle.py` — 8-puzzle solved with BFS and A* (Manhattan distance), with a solvability check.
- `07_magic_squares.py` — Siamese and doubly-even magic square construction and enumeration of all 3x3 squares.
- `08_tower_of_hanoi.py` — Tower of Hanoi recursively and iteratively, with move validation and four-peg Frame-Stewart.
- `09_cryptarithm.py` — Column-by-column cryptarithm solver with carries (SEND + MORE = MONEY and others).
- `10_water_jugs.py` — Water jug puzzles solved by BFS over volume states, with a gcd feasibility test.
- `11_josephus.py` — Josephus problem via deque simulation, linear recurrence and the closed form for k = 2.
- `12_collatz_records.py` — Collatz stopping times with memoization, record holders, peaks and a histogram.
- `13_peg_solitaire.py` — Triangular 15-hole peg solitaire solved with bitboards and memoized DFS.
- `14_river_crossing.py` — Wolf-goat-cabbage and missionaries-and-cannibals puzzles as BFS over states.
- `15_matchstick_equations.py` — Fixing false matchstick equations by moving one stick between seven-segment digits.
- `16_lights_out.py` — Lights Out solved exactly with Gaussian elimination over GF(2) using integer bit rows.
- `17_twenty_four_game.py` — The 24 game solved with exact Fraction arithmetic over all operator trees.
- `18_zebra_puzzle.py` — The Zebra (Einstein) puzzle solved with permutations and pruned generator expressions.
- `19_bridge_and_torch.py` — Bridge and torch puzzle solved with Dijkstra's algorithm over bank states.
- `20_pancake_sorting.py` — Pancake sorting comparing greedy flips with optimal BFS distances.

