## Chapter 7 - Quick references

* [Data types](#types)
* [Creation](#creation)
* [Reshaping](#reshaping)
* [Slicing](#slicing)
* [Broadcasting](#broadcasting)
* [Operations](#operations)

### Data types <a name="types"></a>

| Data type    |  Description                                                         |
|--------------|----------------------------------------------------------------------|
| `bool`       | Boolean (True or False) stored as a byte                             |
| `int`        | Platform integer (normally either int32 or int64)                    |
| `int8`       | Byte (-128 to 127)                                                   |
| `int16`      | Integer (-32768 to 32767)                                            |
| `int32`      | Integer (-2147483648 to 2147483647)                                  |
| `int64`      | Integer (9223372036854775808 to 9223372036854775807)                 |
| `uint8`      | Unsigned integer (0 to 255)                                          |
| `uint16`     | Unsigned integer (0 to 65535)                                        |
| `uint32`     | Unsigned integer (0 to 4294967295)                                   |
| `uint64`     | Unsigned integer (0 to 18446744073709551615)                         |
| `float`      | Shorthand for float64.                                               |
| `float16`    | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa    |
| `float32`    | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa  |
| `float64`    | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa |
| `complex`    | Shorthand for complex128.                                            |
| `complex64`  | Complex number, represented by two 32-bit floats                     |
| `complex128` | Complex number, represented by two 64-bit floats                     |

### Creation <a name="creation"></a>

| Syntax                      | Output                      |
|-----------------------------|-----------------------------|
| `zeros(9)`                  | ![](../pics/creation-1.png) |
| `ones(9)`                   | ![](../pics/creation-2.png) |
| `range(9)`                  | ![](../pics/creation-3.png) |
| `random.randint(0,9,9)`     | ![](../pics/creation-4.png) |
| `zeros((3, 9))`             | ![](../pics/creation-5.png) |
| `ones((3, 9))`              | ![](../pics/creation-6.png) |
| `range(3*9).reshape(3,9)`   | ![](../pics/creation-7.png) |
| `random.randint(0,9,(3,9))` | ![](../pics/creation-8.png) |


### Reshaping <a name="reshaping"></a>
### Slicing <a name="slicing"></a>
### Broadcasting <a name="broadcasting"></a>
### Operations <a name="operations"></a>
