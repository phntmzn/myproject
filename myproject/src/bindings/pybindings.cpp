#include <pybind11/pybind11.h>
#include "mylib/mylib.h"

namespace py = pybind11;

PYBIND11_MODULE(mylib_bindings, m) {
    m.doc() = "Python bindings for mylib";

    m.def("add", &mylib::add, "Add two integers");
}
