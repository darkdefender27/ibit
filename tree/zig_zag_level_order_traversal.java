
/**
 * Author :: @darkdefender27
 * Link :: https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/
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
	public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode a) {

	    ArrayList<ArrayList<Integer>> zigZag = new ArrayList<ArrayList<Integer>>();

	    if(a != null) {
	        Stack<TreeNode> s1 = new Stack<TreeNode>();
	        Stack<TreeNode> s2 = new Stack<TreeNode>();
	        s1.push(a);

	        while(!s1.empty() || !s2.empty()) {

                ArrayList<Integer> level_left = new ArrayList<Integer>();
    	        while(!s1.empty()) {

    	            TreeNode el = s1.pop();
    	            if(el.left != null) s2.push(el.left);
    	            if(el.right != null) s2.push(el.right);

    	            level_left.add(el.val);
    	        }
    	        if(!level_left.isEmpty()) zigZag.add(level_left);

                ArrayList<Integer> level_right = new ArrayList<Integer>();
    	        while(!s2.empty()) {

    	            TreeNode el = s2.pop();
    	            if(el.right != null) s1.push(el.right);
    	            if(el.left != null) s1.push(el.left);

    	            ArrayList<Integer> level = new ArrayList<Integer>();
    	            level_right.add(el.val);
    	        }
    	        if(!level_right.isEmpty()) zigZag.add(level_right);
	        }
	    }

	    return zigZag;
	}
}
