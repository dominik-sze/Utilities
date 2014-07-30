package leetcode;

import org.junit.*;
import static org.junit.Assert.*;


public class SolutionTest {

	@Test
	public void testEmptyArray() {
		int[] num = {};
		Solution s = new Solution();
		TreeNode root = s.sortedArrayToBST(num);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"]";
		String result = t.toString();
		assertEquals(null, root);
		assertEquals(expected, result);
	}

	@Test
	public void testSingleElemArray() {
		int[] num = {3};
		Solution s = new Solution();
		TreeNode root = s.sortedArrayToBST(num);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[3]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testTwoElemArray() {
		int[] num = {3, 4};
		Solution s = new Solution();
		TreeNode root = s.sortedArrayToBST(num);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[3],"+ls+"\t[4]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testThreeElemArray() {
		int[] num = {3, 4, 5};
		Solution s = new Solution();
		TreeNode root = s.sortedArrayToBST(num);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[3],"+ls+"\t[4,5]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}

	@Test
	public void testSixElemArray() {
		int[] num = {3, 4, 5, 7, 12, 99};
		Solution s = new Solution();
		TreeNode root = s.sortedArrayToBST(num);
		LevelOrderTraversal t = new LevelOrderTraversal();
		t.traverse(root, 0);
		String ls = System.lineSeparator();
		String expected = "["+ls+"\t[3],"+ls+"\t[4,5],"+ls+"\t[7,12,99]"+ls+"]";
		String result = t.toString();
		assertEquals(expected, result);
	}
}
