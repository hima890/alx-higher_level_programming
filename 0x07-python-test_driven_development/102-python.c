#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: Pointer to Python object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const char *type;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	type = PyUnicode_IS_COMPACT_ASCII(p) ?
	 "compact ascii" : "compact unicode object";

	printf("  type: %s\n", type);
	printf("  length: %ld\n", length);
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
