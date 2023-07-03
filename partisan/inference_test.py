from polar_func import query

output = query({
    "inputs": "Looks like they are setting up a big “voter dump” against the Republican candidates. Waiting to see how many votes they need?",
    "parameters": {"candidate_labels": ["republican", "democrat"]},
})

print(output)