package leetcode;

import leetcode.binarytree.*;

import org.junit.*;
import static org.junit.Assert.*;


public class LevelOrderTraversalTest {

	@Test
	public void testEmptyTree() {
		TreeNode root = null;
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String expected = "["+System.lineSeparator()+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testRootOnly() {
		TreeNode root = new TreeNode(1);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[1]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testTwoLevels() {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[1],"+ls+"\t[2,3]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}
	
	@Test
	public void testThreeLevels() {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		root.left.right = new TreeNode(5);
		root.right.right = new TreeNode(7);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[1],"+ls+"\t[2,3],"+ls+"\t[4,5,7]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testOnlyRight() {
		TreeNode root = new TreeNode(1);
		root.right = new TreeNode(3);
		root.right.right = new TreeNode(7);
		root.right.right.right = new TreeNode(15);
		root.right.right.right.right = new TreeNode(99);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[1],"+ls+"\t[3],"+ls+"\t[7],"+ls+"\t[15],"+ls+"\t[99]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}
}
