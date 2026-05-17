alias:: [[gotemplate]]
see-also:: [[Go/StdLib/html/template]]

- # Go standard text templating language - [`text/template`](https://pkg.go.dev/text/template)
	- it's similar to [[Mustache]] because it uses double curley braces:
		- ```gotemplate
		  {{ .Name }}
		  {{ if .Condition }}
		  ```
		- but it's not actually mustache
	- it's Go’s own template language
		- Much more powerful than [[Mustache]]
		- Includes conditionals, loops, functions, pipelines, variables, etc.