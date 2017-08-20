/**
 * Author :: @darkdefender27
 *
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
	public int minDepth(TreeNode a) {

	    int minDepth = 0;

	    if(a != null) {

	        Queue<TreeNode> q = new LinkedList<TreeNode>();
    	    q.add(a);

    	    int levelSize = 1;
    	    boolean foundLeafNode = false;

    	    while(!q.isEmpty() && !foundLeafNode) {

    	        minDepth++;

    	        int ct = levelSize;
    	        levelSize = 0;
    	        while(ct>0) {
    	            TreeNode el = q.remove();

        	        if(el.left == null && el.right == null) {
        	            foundLeafNode = true;
        	            break;
        	        }
        	        if(el.left != null) {
        	            q.add(el.left);
        	            levelSize++;
        	        }
        	        if(el.right != null) {
        	            q.add(el.right);
        	            levelSize++;
        	        }
        	        ct--;
    	        }
    	    }
	    }

	    return minDepth;
	}
}
