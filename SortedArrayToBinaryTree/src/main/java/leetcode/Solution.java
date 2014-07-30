package leetcode;


public class Solution {
	int[] vals;
    	public static void main(String[] args) {
	    	TreeNode n = new TreeNode(0);
	    	System.out.println(n.val);
    	}
	public TreeNode sortedArrayToBST(int[] num) {
		int index = 0;
		vals = num;
		TreeNode root = null;
		if(num.length>0) {
			root = new TreeNode(vals[0]);
			insertVal(root, 0);
		}	
	    	return root;
	}

	public void insertVal(TreeNode node, int index) {
		int lindex = 2*index+1;
		int rindex = 2*index+2;
		if(vals.length>lindex) {
			node.left = new TreeNode(vals[lindex]);
			insertVal(node.left, lindex);
		}	
		if(vals.length>rindex) {
			node.right = new TreeNode(vals[rindex]);
			insertVal(node.right, rindex);
		}
	}
}
