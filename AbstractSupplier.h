#pragma once
#include <AbstractProduct.h>

class AbstractSupplier {
public:
    virtual ~AbstractSupplier() = default;
private:
    int prod_cost;
    int gross_cost;
    string name;
    string location;
    AbstractProduct product;
    int capacity;
};