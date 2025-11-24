/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // if (!l1 || !l2) return NULL; // List has no elements

    struct ListNode *p1 = l1;
    struct ListNode *p2 = l2;

    struct ListNode *head = NULL;
    struct ListNode *ant = NULL;
    int carry = 0;

    while (p1 || p2) {
        int val1, val2;
        val1 = p1 ? p1->val : 0;
        val2 = p2 ? p2->val : 0;
        // if (val1 < 0 || val2 < 0) return NULL;
        // if (val1 > 9 || val2 > 9) return NULL;

        struct ListNode *obj = (struct ListNode *)malloc(sizeof(struct ListNode));
        obj->next = NULL;
        int sum = val1 + val2 + carry;
        obj->val = (sum % 10);
        carry = sum / 10;

        if (!ant) {
            head = ant = obj;
        }
        else {
            ant->next = obj;
            ant = obj;
        }

        if (p1) p1 = p1->next;
        if (p2) p2 = p2->next;
    }

    if (carry) {
        struct ListNode *extra = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (!extra) return NULL;
        extra->val  = carry;
        extra->next = NULL;
        ant->next   = extra;
    }

    return head;
}