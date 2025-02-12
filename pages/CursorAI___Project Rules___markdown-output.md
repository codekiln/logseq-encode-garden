description:: If you are outputting markdown, follow these rules
globs:: `*.md,*.mdc`
link:: https://gist.github.com/codekiln/71f9497eaece99ba4d1c95b89d40b315

- # Rules to follow when outputting markdown
- It's important that there is only one level of triple-backtick fenced code blocks in markdown output.
- place your response in a triple-backtick fenced codeblock that's labeled with markdown, and use triple tilde fenced codeblocks for any inner code blocks, as per the CommonMark spec.
- <EXAMPLE>
- ```markdown
  Here's an example of the code: 
      ~~~bash
      $> git describe --tags
      ~~~
  ```
- </EXAMPLE>