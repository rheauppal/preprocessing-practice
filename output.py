                                                text  ...  RDizzl3_seven
0  The Electoral College is a complex system that...  ...           True
1  The exploration of Venus, Earth's closest plan...  ...           True
2  ## Does the Electoral College Work?\n\nThe Ele...  ...           True
3  In the vast realm of literature, there exists ...  ...           True
4  In the realm of modern transportation, the adv...  ...           True

[5 rows x 5 columns]
text             0
label            0
prompt_name      0
source           0
RDizzl3_seven    0
dtype: int64
                                                text  ...                                       text_cleaned
0  The Electoral College is a complex system that...  ...  The Electoral College is a complex system that...
1  The exploration of Venus, Earth's closest plan...  ...  The exploration of Venus, Earth's closest plan...
2  ## Does the Electoral College Work?\n\nThe Ele...  ...  ## Does the Electoral College Work? The Electo...
3  In the vast realm of literature, there exists ...  ...  In the vast realm of literature, there exists ...
4  In the realm of modern transportation, the adv...  ...  In the realm of modern transportation, the adv...

[5 rows x 6 columns]
                                                text  ...  urls
0  The Electoral College is a complex system that...  ...    []
1  The exploration of Venus, Earth's closest plan...  ...    []
2  ## Does the Electoral College Work?\n\nThe Ele...  ...    []
3  In the vast realm of literature, there exists ...  ...    []
4  In the realm of modern transportation, the adv...  ...    []

[5 rows x 7 columns]
                                                text  ...  urls
0  The Electoral College is a complex system that...  ...    []
1  The exploration of Venus, Earth's closest plan...  ...    []
2  ## Does the Electoral College Work?\n\nThe Ele...  ...    []
3  In the vast realm of literature, there exists ...  ...    []
4  In the realm of modern transportation, the adv...  ...    []

[5 rows x 7 columns]
Rows where 'text_cleaned' column contains lists:
Empty DataFrame
Columns: [text, label, prompt_name, source, RDizzl3_seven, text_cleaned, urls]
Index: []
Toxicity Scores:
                                                text  toxicity
0  The Electoral College is a complex system that...  0.000863
1  The exploration of Venus, Earth's closest plan...  0.000635
2  ## Does the Electoral College Work?\n\nThe Ele...  0.000864
3  In the vast realm of literature, there exists ...  0.001228
4  In the realm of modern transportation, the adv...  0.000752
Subjectivity Scores:
                                                text  subjectivity
0  The Electoral College is a complex system that...      0.493235
1  The exploration of Venus, Earth's closest plan...      0.612145
2  ## Does the Electoral College Work?\n\nThe Ele...      0.448100
3  In the vast realm of literature, there exists ...      0.626344
4  In the realm of modern transportation, the adv...      0.606909
Text Chunks:
                                        text_cleaned                                        text_chunks
0  The Electoral College is a complex system that...  [<s>The Electoral College is a complex system ...
1  The exploration of Venus, Earth's closest plan...  [<s>The exploration of Venus, Earth's closest ...
2  ## Does the Electoral College Work? The Electo...  [<s>## Does the Electoral College Work? The El...
3  In the vast realm of literature, there exists ...  [<s>In the vast realm of literature, there exi...
4  In the realm of modern transportation, the adv...  [<s>In the realm of modern transportation, the...
Formality Scores:
                                                text formality  formality_score
0  The Electoral College is a complex system that...    formal         0.996824
1  The exploration of Venus, Earth's closest plan...    formal         0.997044
2  ## Does the Electoral College Work?\n\nThe Ele...    formal         0.996904
3  In the vast realm of literature, there exists ...    formal         0.956150
4  In the realm of modern transportation, the adv...    formal         0.997210
Redundancy Scores:
                                                text  redundancy_score
0  The Electoral College is a complex system that...          0.131579
1  The exploration of Venus, Earth's closest plan...          0.044343
2  ## Does the Electoral College Work?\n\nThe Ele...          0.098712
3  In the vast realm of literature, there exists ...          0.017199
4  In the realm of modern transportation, the adv...          0.093168
