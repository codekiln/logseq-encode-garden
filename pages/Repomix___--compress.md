# [Repomix Code Compression](https://github.com/yamadashy/repomix/tree/main?tab=readme-ov-file#code-compression) - `repomix --compress`
	- ## [[My Notes]]
	  id:: 67c7f234-c55c-4b12-a260-d92aa3cfbb0c
		- Uses [[Tree-Sitter]] to "compress" code by reducing it to function signatures
		- potentially #Cool - though I can imagine how this might confuse an engineer that didn't understand the implication of how this feature would impact what the AI "understands" about the context from the generated repomix file.
		- Reminds me of a [[QodoAI]] demo I saw in a webinar where they discussed a similar [[Embedding Chunking]] strategy. Theirs was bit more intelligent, I think, and could create a chunk for each class's method which was a tiny, compressed version of the class with attributes and referenced function signatures with commented out method bodies. I think they used multi-layered chunking to ensure AI could get the "gist" of the code when a single chunk was returned from a [[Vector DB]]
	- uses [[Tree-Sitter]] to perform a form of code compression that transforms this
		- ```typescript
		  const calculateTotal = (items: ShoppingItem[]) => {
		    let total = 0;
		    for (const item of items) {
		      total += item.price * item.quantity;
		    }
		    return total;
		  }
		  interface Item {
		    name: string;
		    price: number;
		    quantity: number;
		  }
		  ```
	- into this
		- ```typescript
		  const calculateTotal = (items: ShoppingItem[]) => {
		  interface Item {
		  ```