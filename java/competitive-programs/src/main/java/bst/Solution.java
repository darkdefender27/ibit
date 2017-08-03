package bst;

import bst.model.BinarySearchTree;
import bst.model.Node;

/**
 * Created by shubhamutwal on 03/08/17.
 */
public class Solution {

    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree(null);

        bst.put(2);
        bst.put(1);
        bst.put(4);
        bst.put(3);
        bst.put(0);

        Node rootNode = bst.getRoot();
        System.out.println("Root Node: " + rootNode.getValue());

        if(bst.contains(4)) {
            System.out.println("Node present!");
        } else {
            System.out.println("Node absent!");
        }
    }
}
