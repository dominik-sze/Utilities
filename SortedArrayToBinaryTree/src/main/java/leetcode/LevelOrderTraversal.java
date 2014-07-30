package leetcode;

import java.util.*;


public class LevelOrderTraversal {
	List<List<Integer>> tree;

	public LevelOrderTraversal() {
		tree = new ArrayList<List<Integer>>();
	}
	
	public void traverse(TreeNode node, int level) {
		if(node == null) {
			return;
		} else {
			if(tree.size()==level) {
				tree.add(new ArrayList<Integer>());
			}
			tree.get(level).add(node.val);
		}
		if(node.left!=null) {
			traverse(node.left, level+1);
		}
		if(node.right!=null) {
			traverse(node.right, level+1);
		}
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder("[");
		sb.append(System.lineSeparator());
		if(tree.size()>0) {
			for(int i=0; i<tree.size(); i++) {
				sb.append("\t[");
				for(int j=0; j<tree.get(i).size(); j++) {
					if(j==tree.get(i).size()-1) {
						sb.append(tree.get(i).get(j));
					} else {
						sb.append(tree.get(i).get(j)+",");
					}
				}
				if(i==tree.size()-1) {
					sb.append("]"+System.lineSeparator());
				} else {
					sb.append("],"+System.lineSeparator());
				}
			}
		}
		sb.append("]");
		return sb.toString();
	}
}
