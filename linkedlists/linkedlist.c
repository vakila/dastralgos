#include<stdio.h>

typedef struct node
{
    int value;
    struct node* next; // this is a pointer to the next node in the list
} node;

int main(int argc, char* argv[])
{
    node node1;
    node node2;
    node node3;

    node1.value = 10;
    node2.value = 20;
    node3.value = 30;

    node1.next = &node2;
    node2.next = &node3;
    node3.next = 0;

    printf("list contents:\n");
    node* current_node_pointer = &node1;
    while(current_node_pointer != 0)
    {
        printf("%d\n", current_node_pointer->value);
        current_node_pointer = current_node_pointer->next;
    }

    // move node3 to the middle
    node* p;
    p = &node3;
    node3.next = &node2;
    node1.next = &node3;
    node2.next = 0;

    printf("list contents:\n");
    current_node_pointer = &node1;
    while(current_node_pointer != 0)
    {
        printf("%d\n", current_node_pointer->value);
        current_node_pointer = current_node_pointer->next;
    }
}
