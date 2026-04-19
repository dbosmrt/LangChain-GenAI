"""
Text splitting is the process of breking large chunks of text(like articles, PDFs, HTML pages, or books)
into smaller, manageable pieces(chunks) that an LLM can handle effectively.

Overcoming model limitation: May embedding models and language models
have maximum input size constraints. Splitting allows us to precess documents,
that would otherwise exceed these limits.

Downstream Tasks - Text Splitting improves nearlh every LLM powered task

Optimizing computational resources: Working with the smaller chunks of text can be 
more memory - eficient and allow for better paralleliztion of processing tasks.
"""
"""
Length based text splitting - We define the size of the chunks which will be uniform for all of the chunks.

Chunk overlap - tells you the overlap between the cunks.

Text-Structured Based - Organize the text structure. (recursive character text splitting.)
Here we define the seaparators (\n\n , \n, ' ')
"""
"""
Document-Structured Based
"""
"""
Semantic Meaning Based
Farmers were working hard in the felds, preparing the soil and planting seeds for
the next searson, the sun was bright, and the air smelled of earth and fresh grass.
The Indian Premier League(IPL) is the biggest cricekt league in the world. People all over the
world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates
fear in cities and villages. When such attacks happen, they leave behind pain and 
sadness. To fight terrorism, we need strong laws, alert security forces, and support
from people who care about peace and saftey.

we can use silimalirty window approach...
"""



