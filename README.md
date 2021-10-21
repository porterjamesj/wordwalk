# Word Walk

Create `lexvec_words_only.txt` from `lexvec.enwiki+newscrawl.300d.W.pos.vectors ~/src/words` using this command:

```bash
cut -d ' ' -f 1 < lexvec.enwiki+newscrawl.300d.W.pos.vectors > lexvec_words_only.txt
```
