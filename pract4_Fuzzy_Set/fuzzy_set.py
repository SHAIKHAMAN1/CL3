# Assignment No: 04
# Title: Fuzzy Set Operations + Fuzzy Relations
# B.E. (AI&DS) - Computer Laboratory III

def get_fuzzy_set(name):
    s = {}
    n = int(input(f"How many elements in Fuzzy Set {name}? "))
    for _ in range(n):
        elem = input(f"  Element name: ")
        deg  = float(input(f"  Membership degree for '{elem}' (0-1): "))
        s[elem] = deg
    return s

def fuzzy_union(A, B):
    keys = set(A) | set(B)
    return {k: max(A.get(k, 0), B.get(k, 0)) for k in sorted(keys)}

def fuzzy_intersection(A, B):
    keys = set(A) | set(B)
    return {k: min(A.get(k, 0), B.get(k, 0)) for k in sorted(keys)}

def fuzzy_complement(A):
    return {k: round(1 - v, 4) for k, v in A.items()}

def fuzzy_difference(A, B):
    keys = set(A) | set(B)
    return {k: round(min(A.get(k, 0), 1 - B.get(k, 0)), 4) for k in sorted(keys)}

def cartesian_product(A, B):
    return {(x, y): round(min(ux, uy), 4) for x, ux in A.items() for y, uy in B.items()}

def max_min_composition(R, S, A_keys, B_keys, C_keys):
    return {
        (x, z): round(max(min(R[(x, y)], S[(y, z)]) for y in B_keys), 4)
        for x in A_keys for z in C_keys
    }

def print_relation(name, relation, row_keys, col_keys):
    print(f"\n{name}:")
    print(f"{'':>5}" + "".join(f"{c:>8}" for c in col_keys))
    for r in row_keys:
        print(f"{r:>5}" + "".join(f"{relation[(r, c)]:>8}" for c in col_keys))


# ─────────────────────────────────────────────
# PART 1: FUZZY SET OPERATIONS
# ─────────────────────────────────────────────
print("=" * 50)
print("       FUZZY SET OPERATIONS")
print("=" * 50)

A = get_fuzzy_set("A")
print()
B = get_fuzzy_set("B")

print(f"\nFuzzy Set A : {A}")
print(f"Fuzzy Set B : {B}")

print("\n--- 1. Union ---")
print(f"A U B = {fuzzy_union(A, B)}")

print("\n--- 2. Intersection ---")
print(f"A n B = {fuzzy_intersection(A, B)}")

print("\n--- 3. Complement of A ---")
print(f"A'    = {fuzzy_complement(A)}")

print("\n--- 4. Difference (A - B) ---")
print(f"A - B = {fuzzy_difference(A, B)}")


# ─────────────────────────────────────────────
# PART 2: FUZZY RELATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("       FUZZY RELATIONS")
print("=" * 50)
print("\nEnter 3 fuzzy sets X, Y, Z for relations:\n")

X = get_fuzzy_set("X")
print()
Y = get_fuzzy_set("Y")
print()
Z = get_fuzzy_set("Z")

print(f"\nSet X : {X}")
print(f"Set Y : {Y}")
print(f"Set Z : {Z}")

R = cartesian_product(X, Y)
print_relation("Relation R = X x Y", R, list(X.keys()), list(Y.keys()))

S = cartesian_product(Y, Z)
print_relation("Relation S = Y x Z", S, list(Y.keys()), list(Z.keys()))

T = max_min_composition(R, S, list(X.keys()), list(Y.keys()), list(Z.keys()))
print_relation("Composition T = R o S  (Max-Min)", T, list(X.keys()), list(Z.keys()))

print("\n" + "=" * 50)
print("Conclusion: Fuzzy set operations and fuzzy")
print("relations implemented successfully.")
print("=" * 50)


''''''
Sample Input:
For A and B
3
a
0.2
b
0.8
c
0.5

For Relation 
2, x1, x2, y1, y2, z1, z2
'''