# DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC email authentication module implemented in Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dmarc.

```bash
pip install dmarc
```

## Usage

```python
>>> import dmarc
>>>
>>> # represent verified SPF and DKIM status
>>> aspf = dmarc.SPF(domain='news.example.com', result=dmarc.SPF_PASS)
>>> adkim = dmarc.DKIM(domain='example.com', result=dmarc.DKIM_PASS)
>>> try:
...     admarc = dmarc.DMARCPolicy(record='v=DMARC1; p=reject;', domain='example.com')
...     admarc.verify(spf=aspf, dkim=adkim)
...     adict = admarc.result.as_dict() # dict repr
... except dmarc.PolicyNoneError:
...     pass
... except dmarc.PolicyQuarantineError:
...     raise
... except dmarc.PolicyRejectError:
...     raise
... except dmarc.RecordSyntaxError:
...     raise
...
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
