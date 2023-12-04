#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = Py_SIZE(p);
	list = (PyListObject *)p;

	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
