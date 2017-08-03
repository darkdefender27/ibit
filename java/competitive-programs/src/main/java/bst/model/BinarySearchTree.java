package bst.model;

import bst.exceptions.EmptyTreeException;
import bst.exceptions.InvalidValueException;

/**
 * Created by shubhamutwal on 03/08/17.
 */
public class BinarySearchTree {

    private static final String EMPTY_TREE_MSG = "You've found an empty tree.";
    private static final String INVALID_VALUE_MSG = "Invalid value present in the tree.";

    private Node root;

    public BinarySearchTree(Node root) {
        this.root = root;
    }

    public Node getRoot() {
        if(this.root == null) {
            throw new EmptyTreeException(EMPTY_TREE_MSG);
        }
        return this.root;
    }

    public boolean contains(int value) {

        boolean isPresent = false;

        if(this.root == null) {
            throw new EmptyTreeException(EMPTY_TREE_MSG);
        } else {
            Node temp = this.root;
            while(temp != null) {
                if(temp.getValue() != null && temp.getValue() < value) {
                    temp = temp.getRight();
                } else if(temp.getValue() != null && temp.getValue() > value) {
                    temp = temp.getLeft();
                } else if(temp.getValue() != null && temp.getValue() == value) {
                    isPresent = true;
                    break;
                }
            }
        }

        return isPresent;
    }

    public void put(Integer value) {

        if(value == null) {
            throw new InvalidValueException(INVALID_VALUE_MSG);
        } else {
            this.putRecursive(this.root, value);
        }
    }

    public void putRecursive(Node rootNode, Integer value) {

        if(rootNode == null) {
            this.root = new Node(value, null, null);
        } else if(rootNode.getLeft() == null && rootNode.getValue() >= value) {
            rootNode.setLeft(new Node(value, null, null));
        } else if(rootNode.getRight() == null && rootNode.getValue() < value) {
            rootNode.setRight(new Node(value, null, null));
        } else {
            if(rootNode.getValue() < value) {
                putRecursive(rootNode.getRight(), value);
            } else {
                putRecursive(rootNode.getLeft(), value);
            }
        }
    }

    public void putIterative(Integer value) {

        if(value == null) {
            throw new InvalidValueException(INVALID_VALUE_MSG);
        }

        Node newNode = new Node(value, null, null);

        if(this.root == null) {
            this.root = newNode;
        } else {
            Node temp = this.root;
            while(true) {
                if(temp.getValue() != null && temp.getValue() < value) {
                    if(temp.getRight() != null) {
                        temp = temp.getRight();
                    } else {
                        temp.setRight(newNode);
                        break;
                    }
                } else if(temp.getValue() != null && temp.getValue() >= value) {
                    if(temp.getLeft() != null) {
                        temp = temp.getLeft();
                    } else {
                        temp.setLeft(newNode);
                        break;
                    }
                }
            }
        }
    }
}
