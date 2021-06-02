import java.io.IOException;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;

class Node<T> {
	T item;
	Node next;

	Node(T item) {
		this.item = item;
	}
}

class Set<T> {
	int size;
	int TABLE_SIZE = 193;
	Node [] table;
	int type;

	Set() {
		size = 0;
		table = new Node [TABLE_SIZE];
		reset();
	}

	void reset() {
		for (int i = 0; i < TABLE_SIZE; i++) {
			table[i] = null;
		}
		size = 0;
	}
	// INSERT
	boolean insert(T item) {
		int hash = getHash(item);
		if(table[hash] == null) {
			table[hash] = new Node(item);
		} else {
			Node element = table[hash];
			while(element.next != null && !element.item.equals(item))
				element = element.next;
			if(element.item.equals(item))
				return false;
			else
				element.next = new Node(item);
		}
		size++;
		return true;
	}
	// REMOVE
	boolean remove(T item) {
		int hash = getHash(item);
		if(table[hash] == null) {
			return false;
		} else {
			Node prevElement = null;
			Node element = table[hash];
			while(element.next != null && !element.item.equals(item)) {
				prevElement = element;
				element = element.next;
			}
			if(element.item.equals(item)) {
				if(prevElement == null)
					table[hash] = element.next;
				else
					prevElement.next = element.next;
				size--;
			}
		}
		return true;
	}
	// SUBSET
	boolean subSet(Set <T> set) {
		if(this.size > set.size) {
			return false;
		} else {
			for(int i = 0; i < TABLE_SIZE; i++) {
				Node element = table[i];
				while(element != null) {
					if(!(set.isElement((T)element.item)))
						return false;
					element = element.next;
				}
			}
		}
		return true;
	}
	// UNION
	Set <T> union(Set <T> set) {
		Set <T> newSet = new Set <T>();
		for(int i = 0; i < TABLE_SIZE; i++) {
			Node element = table[i];
			while(element != null) {
				newSet.insert((T)element.item);
				element = element.next;
			}
		}
		for(int i = 0; i < set.TABLE_SIZE; i++) {
			Node element = set.table[i];
			while(element != null) {
				newSet.insert((T)element.item);
				element = element.next;
			}
		}
		return newSet;
	}
	// INTERSECTION
	Set <T> intersection(Set <T> set) {
		Set <T> newSet = new Set <T>();
		for(int i = 0; i < TABLE_SIZE; i++) {
			Node element = table[i]; 
			while(element != null) {
				if(set.isElement((T)element.item))
					newSet.insert((T)element.item);
				element = element.next;
			}
		}
		return newSet;
	}
	// DIFFERENCE
	Set <T> difference(Set <T> set) {
		Set <T> newSet = new Set <T>();
		for(int i = 0; i < TABLE_SIZE; i++) {
			Node element = table[i]; 
			while(element != null) {
				if(!set.isElement((T)element.item))
					newSet.insert((T)element.item);
				element = element.next;
			}
		}
		return newSet;
	}
	// POWERSET
	String powerSet() {
		String powerset = "{";
		powerset += "empty";
		LinkedList<Node> list = getList();
		LinkedList<String> subsets = new LinkedList<String>();
		int sizeY = 0;

		for(int i = 0; i < list.size(); i++) {
			sizeY = subsets.size();
			subsets.add("" + list.get(i).item);
			powerset += ",";
			powerset += "{" + list.get(i).item + "}";
			for(int j = 0; j < sizeY; j++) {
				subsets.add(subsets.get(j) + "," + list.get(i).item);
				powerset += ",{" + subsets.get(j) + "," + list.get(i).item + "}";
			}
		}
		powerset += "}";
		return powerset;
	}

	int getHash(T item) {
		int hash = item.hashCode() % TABLE_SIZE;
		if(hash < 0)
			hash += TABLE_SIZE;
		return hash;
	}

	public String toString() {
		String set = "{";
		for(int i = 0, count = 0; i < TABLE_SIZE; i++) {
			Node entry = table[i];
			while(entry != null) {
				count++;
				set += entry.item;
				entry = entry.next;
				if(count < this.size)
					set += ",";
			}
		}
		set += "}";
		return set;
	}

	boolean isElement(T item) {
		int hash = getHash(item);
		if(table[hash] == null)
			return false;
		else {
			Node element = table[hash];
			while(element.next != null && !element.item.equals(item))
				element = element.next;
			if(!element.item.equals(item))
				return false;
		}
		return true;
	}

	LinkedList <Node> getList() {
		LinkedList<Node> linkedlist = new LinkedList<Node>();
		for(int i = 0; i < TABLE_SIZE; i++) {
			Node element = table[i]; 
			while(element != null) {
				linkedlist.add(element);
				element = element.next;
			}
		}
		return linkedlist;  
	}
}

class SetOperations {

	private static final String FILENAME = "mpa1.in";
	private static final String FILEOUT = "bagaipo.out";

	public static void main(String[] args) {
		BufferedReader br = null;
		FileReader fr = null;
		BufferedWriter bw = null;
		FileWriter fw = null;
		
		Set <Integer> i_set1 = new Set <Integer>();
		Set <Integer> i_set2 = new Set <Integer>();
		Set <Double> d_set1 = new Set <Double>();
		Set <Double> d_set2 = new Set <Double>();
		Set <Character> c_set1 = new Set <Character>();
		Set <Character> c_set2 = new Set <Character>(); 
		Set <String> s_set1 = new Set <String>();
		Set <String> s_set2 = new Set <String>(); 
		Set <String> set1 = new Set <String>();
		Set <String> set2 = new Set <String>();

		try {
			fr = new FileReader(FILENAME);
			br = new BufferedReader(fr);
			br = new BufferedReader(new FileReader(FILENAME));
			fw = new FileWriter(FILEOUT);
			bw = new BufferedWriter(fw);

			String sCurrentLine;
			String[] inputLine;
			int testCases = Integer.parseInt(br.readLine());
			int line;
		
			while (testCases > 0) {
				line = 0;
				int elementType = 0;
				int operations = 0;
				i_set1 = new Set <Integer>();
				i_set2 = new Set <Integer>();
				d_set1 = new Set <Double>();
				d_set2 = new Set <Double>();
				c_set1 = new Set <Character>();
				c_set2 = new Set <Character>(); 
				s_set1 = new Set <String>();
				s_set2 = new Set <String>(); 
				set1 = new Set <String>();
				set2 = new Set <String>();

				while ((sCurrentLine = br.readLine()) != null) {
					inputLine = sCurrentLine.split(" ");
					line++;
					elementType = elementType;
					if (line == 1) {
						elementType = Integer.parseInt(inputLine[0]);
					} else if (line == 2 || line == 3) {
						
						switch (elementType) {
							case 1: 
								for (int i = 0; i < inputLine.length; i++) {
									if (line == 2) {
										i_set1.insert(Integer.parseInt(inputLine[i]));
									} else if (line == 3) {
										i_set2.insert(Integer.parseInt(inputLine[i]));
									}
								}
								break;
							case 2:
								for (int i = 0; i < inputLine.length; i++) {
									if (line == 2) {
										d_set1.insert(Double.parseDouble(inputLine[i]));
									} else if (line == 3) {
										d_set2.insert(Double.parseDouble(inputLine[i]));
									}
								} 
								break;
							case 3:
								for (int i = 0; i < inputLine.length; i++) {
									if (line == 2) {
										c_set1.insert(inputLine[i].charAt(0));
									} else if (line == 3) {
										c_set2.insert(inputLine[i].charAt(0));
									}
								} 
								break; 
							case 4: 
								for (int i = 0; i < inputLine.length; i++) {
									if (line == 2) {
										s_set1.insert(inputLine[i]);
									} else if (line == 3) {
										s_set2.insert(inputLine[i]);
									}
								} 
								break; 
							case 5: 
								for (int i = 0; i < inputLine.length; i++) {
									if (line == 2) {
										set1.insert(inputLine[i]);
									} else if (line == 3) {
										set2.insert(inputLine[i]);
									}
								} 
								break;
						}

					}	 else if (line == 4) {
						operations = Integer.parseInt(inputLine[0]);
					} else if (line > 4) {
						int op = Integer.parseInt(inputLine[0]);

						switch (op) {
							case 1: // INSERT
								int set = Integer.parseInt(inputLine[1]);
								switch (elementType) { 
									case 1: // if integer
										if (set == 1) {
											i_set1.insert(Integer.parseInt(inputLine[2]));
											bw.write("" + i_set1);
										} else if (set == 2) {
											i_set2.insert(Integer.parseInt(inputLine[2]));
											bw.write("" + i_set2);
										}
										break;
									case 2: // if double
										if (set == 1) {
											d_set1.insert(Double.parseDouble(inputLine[2]));
											bw.write("" + d_set1);
										} else if (set == 2) {
											d_set2.insert(Double.parseDouble(inputLine[2]));
											bw.write("" + d_set2);
										}
										break;
									case 3:
										if (set == 1) {
											c_set1.insert(inputLine[2].charAt(0));
											bw.write("" + c_set1);
										} else if (set == 2) {
											c_set2.insert(inputLine[2].charAt(0));
											bw.write("" + c_set2);
										}
										break;
									case 4:
										if (set == 1) {
											s_set1.insert(inputLine[2]);
											bw.write("" + s_set1);
										} else if (set == 2) {
											s_set2.insert(inputLine[2]);
											bw.write("" + s_set2);
										}
										break;
									case 5:
										if (set == 1) {
											set1.insert(inputLine[2]);
											bw.write("" + set1);
										} else if (set == 2) {
											set2.insert(inputLine[2]);
											bw.write("" + set2);
										}
										break;
								}
								break;
							case 2: // REMOVE
								int setr = Integer.parseInt(inputLine[1]);
								switch (elementType) { 
									case 1: // if integer
										if (setr == 1) {
											i_set1.remove(Integer.parseInt(inputLine[2]));
											bw.write("" + i_set1);
										} else if (setr == 2) {
											i_set2.remove(Integer.parseInt(inputLine[2]));
											bw.write("" + i_set2);
										}
										break;
									case 2: // if double
										if (setr == 1) {
											d_set1.remove(Double.parseDouble(inputLine[2]));
											bw.write("" + d_set1);
										} else if (setr == 2) {
											d_set2.remove(Double.parseDouble(inputLine[2]));
											bw.write("" + d_set2);
										}
										break;
									case 3:
										if (setr == 1) {
											c_set1.remove(inputLine[2].charAt(0));
											bw.write("" + c_set1);
										} else if (setr == 2) {
											c_set2.remove(inputLine[2].charAt(0));
											bw.write("" + c_set2);
										}
										break;
									case 4:
										if (setr == 1) {
											s_set1.remove(inputLine[2]);
											bw.write("" + s_set1);
										} else if (setr == 2) {
											s_set2.remove(inputLine[2]);
											bw.write("" + s_set2);
										}
										break;
									case 5:
										if (setr == 1) {
											set1.remove(inputLine[2]);
											bw.write("" + set1);
										} else if (setr == 2) {
											set2.remove(inputLine[2]);
											bw.write("" + set2);
										}
										break;
								}
								break;
							case 3:	// SUBSET
								switch (elementType) { 
									case 1: // if integer
										bw.write("" + i_set1.subSet(i_set2));
										break;
									case 2: // if double
										bw.write("" + d_set1.subSet(d_set2));
										break;
									case 3:
										bw.write("" + c_set1.subSet(c_set2));
										break;
									case 4:
										bw.write("" + s_set1.subSet(s_set2));
										break;
									case 5:
										bw.write("" + set1.subSet(set2));
										break;
								}
								break;
							case 4: // UNION
								switch (elementType) { 
									case 1: // if integer
										bw.write("" + i_set1.union(i_set2));
										break;
									case 2: // if double
										bw.write("" + d_set1.union(d_set2));
										break;
									case 3:
										bw.write("" + c_set1.union(c_set2));
										break;
									case 4:
										bw.write("" + s_set1.union(s_set2));
										break;
									case 5:
										bw.write("" + set1.union(set2));
										break;
								}
								break;
							case 5: // INTERSECTION
								switch (elementType) { 
									case 1: // if integer
										bw.write("" + i_set1.intersection(i_set2));
										break;
									case 2: // if double
										bw.write("" + d_set1.intersection(d_set2));
										break;
									case 3:
										bw.write("" + c_set1.intersection(c_set2));
										break;
									case 4:
										bw.write("" + s_set1.intersection(s_set2));
										break;
									case 5:
										bw.write("" + set1.intersection(set2));
										break;
								}
								break;
							case 6: // SYMMETRIC DIFFERENCE
								switch (elementType) { 
									case 1: // if integer
										bw.write("" + i_set1.difference(i_set2));
										break;
									case 2: // if double
										bw.write("" + d_set1.difference(d_set2));
										break;
									case 3:
										bw.write("" + c_set1.difference(c_set2));
										break;
									case 4:
										bw.write("" + s_set1.difference(s_set2));
										break;
									case 5:
										bw.write("" + set1.difference(set2));
										break;
								}
								break;
							case 7:	// POWERSET
								int setS = Integer.parseInt(inputLine[1]);
								switch (elementType) { 
									case 1: // if integer
										if (setS == 1) {
											bw.write("" + i_set1.powerSet());
										} else if (setS == 2) {
											bw.write("" + i_set2.powerSet());
										}
										break;
									case 2: // if double
										if (setS == 1) {
											bw.write("" + d_set1.powerSet());
										} else if (setS == 2) {
											bw.write("" + d_set2.powerSet());
										}
										break;
									case 3:
										if (setS == 1) {
											bw.write("" + c_set1.powerSet());
										} else if (setS == 2) {
											bw.write("" + c_set2.powerSet());
										}
										break;
									case 4:
										if (setS == 1) {
											bw.write("" + s_set1.powerSet());
										} else if (setS == 2) {
											bw.write("" + s_set2.powerSet());
										}
										break;
									case 5:
										if (setS == 1) {
											bw.write("" + set1.powerSet());
										} else if (setS == 2) {
											bw.write("" + set2.powerSet());
										}
										break;
								}
								break;
						}
						bw.write("\n");
						operations--;
						if (operations == 0)
							break;
					}
				}
				testCases--;
			}
		}
		 catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
				if (fr != null)
					fr.close();
				if (bw != null)
					bw.close();
				if (fw != null)
					fw.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}
