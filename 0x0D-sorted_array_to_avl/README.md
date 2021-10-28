# 0x0D. Array to AVL

## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be compiled on `Ubuntu 14.04 LTS`
+ Your programs and functions will be compiled with `gcc 4.8.4` using the flags `-Wall` `-Werror` `-Wextra` and `-pedantic`
+ All your files should end with a new line
+ A `README.md` file, at the root of the folder of the project, is mandatory
+ Your code should use the `Betty` style. It will be checked using `betty-style.pl` and `betty-doc.pl`
+ You are not allowed to use global variables
+ No more than 5 functions per file
+ You are allowed to use the standard library

### More Info

#### Data structures

Please use the following data structures and types for binary trees. Don’t forget to include them in your header file.

#### Basic Binary Tree

```c
/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

typedef struct binary_tree_s binary_tree_t;
```

#### AVL Tree

```c
typedef struct binary_tree_s avl_t;
```

### TASKS

1. AVL - From sorted array

Write a function that builds an AVL tree from an array

+ Prototype: `avl_t *sorted_array_to_avl(int *array, size_t size);`
+ Where `array` is a pointer to the first element of the array to be converted
+ And `size` is the number of element in the array
+ Your function must return a pointer to the root node of the created AVL tree, or `NULL` on failure
+ You can assume there will be no duplicate value in the array
+ You are not allowed to rotate
+ You can only have 3 functions in your file

## AUTHOR

### JACKSON MORENO
