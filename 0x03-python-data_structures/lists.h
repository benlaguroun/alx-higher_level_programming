#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 *struct listint_s - Structure for a singly linked list
 *@n: Integer value stored in the node
 *@next: Pointer to the next node in the list
 *Description: Defines the structure of a node in a singly linked list.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */

