from random import randint


# s = secret, n = total number of pieces, k = minimum required
def deconstruct(secret, n, k):
    values = []
    for i in range(n):
        values.append((i+1, polynomial(i+1, k, secret)))
    return tuple(values)


def return_coefficients(k):
    coefficients = []
    for i in range(k-1):
        coefficients.append(randint(1, 100000))
    # return coefficients
    return [166, 94]


def polynomial(d, k, secret):
    coefficients = return_coefficients(k)
    for i in range(len(coefficients)):
        secret += coefficients[i] * d**(i+1)
    return secret


# can be any number of shards
def calculate_lemma(i):
    pass


def reconstruct(*shards):
    print 'size of polynomial: ', len(shards)
    polynomials = []
    lagrange_basis_polynomial(shards)

    # extrapolate the values = x0, x1...xn
    # find the polynomial
    # find the coefficients and constant
    # return the constant/secret
    return True


def lagrange_basis_polynomial(*shards):
    # calculate coefficients of polynomials - zeroth most element is the secret
    # extract x0, x1...xn
    x_values = []
    for i in shards:
        x_values.append(i[0])
    print x_values
    return x_values

# wiki sample
print deconstruct(1234, 6, 3)

reconstruct((1, 2), (34, 4))


