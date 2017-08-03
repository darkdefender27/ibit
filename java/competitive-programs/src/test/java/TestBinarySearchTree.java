import bst.exceptions.EmptyTreeException;
import bst.exceptions.InvalidValueException;
import bst.model.BinarySearchTree;
import bst.model.Node;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by shubhamutwal on 03/08/17.
 */
public class TestBinarySearchTree {

    private BinarySearchTree binarySearchTree;

    @Before
    public void initTest() {
        binarySearchTree = new BinarySearchTree(null);
    }

    @Test
    public void testBinarySearchTreeGetRoot_ShouldReturnRootNode_IfTreeIsNotEmpty() {
        binarySearchTree.put(0);
        Node rootNode = binarySearchTree.getRoot();

        assertNotNull(rootNode);
        assertEquals(new Integer(0), rootNode.getValue());
    }

    @Test(expected = EmptyTreeException.class)
    public void testBinarySearchTreeGetRoot_ShouldThrowEmptyTreeException_IfRootIsNull() {
        binarySearchTree.getRoot();
    }

    @Test
    public void testBinarySearchTreePut_ShouldInsertAnElementInExistingTree_IfNodeWithValidValueIsPassed() {
        binarySearchTree.put(10);

        assertTrue(binarySearchTree.contains(10));
        assertNotNull(binarySearchTree.getRoot());
    }

    @Test(expected = InvalidValueException.class)
    public void testBinarySearchTreePut_ShouldThrowException_IfNodeWithInValidValueIsPassed() {
        binarySearchTree.put(null);
    }

    @Test
    public void testBinarySearchTreeContains_ShouldReturnFalse_IfTreeIsNotEmptyAndNodeIsNotPresentInTree() {
        binarySearchTree.put(2);
        binarySearchTree.put(1);
        binarySearchTree.put(4);
        binarySearchTree.put(3);

        assertFalse(binarySearchTree.contains(0));
        assertFalse(binarySearchTree.contains(100));
        assertFalse(binarySearchTree.contains(-1));
    }

    @Test
    public void testBinarySearchTreeContains_ShouldReturnTrue_IfTreeIsNotEmptyAndNodeIsPresentInTree() {
        binarySearchTree.put(2);
        binarySearchTree.put(1);
        binarySearchTree.put(4);
        binarySearchTree.put(3);
        binarySearchTree.put(0);

        assertTrue(binarySearchTree.contains(1));
        assertTrue(binarySearchTree.contains(0));
        assertTrue(binarySearchTree.contains(4));
        assertTrue(binarySearchTree.contains(2));
        assertTrue(binarySearchTree.contains(3));
    }

    @Test(expected = EmptyTreeException.class)
    public void testBinarySearchTreeContains_ShouldThrowException_IfTreeIsEmpty() {
        assertFalse(binarySearchTree.contains(1));
    }
}
