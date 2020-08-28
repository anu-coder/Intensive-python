### Data sciency things TODO: </br>
**Warning**: very random

1. Jupyter notebook extensions/proper setup and workflow
2. Apply algos like CDD, CWD on dataframes which require for loops
3. Get specific row indices of a df using iloc
4. A workflow to download a file using urllib/requests library
5. A workflow to catch api response using urllib/requests library
6. A workflow to extract information from HTML source using BeautifulSoup
7. Reading files using numpy with different datatypes (np.void)
8. Twitter API StreamListener Class.
9. How does OAuth work?
10. Understanding of HTTP, Requests, API, JSON, HTML
11. Workflow to connect/query/manipulate databases using Python: sqlalchemy (Use contextmanager + using pd.read_sql_query)
12. Proper examples of data cleaning/ data preparation workflow.
    * Missing values-filling/dropping/counting/groupby/recoding
    * Dropping missing values along axis = [0, 1] with criteria how = ['any', 'all']
    * outliers/duplicate-rows/Untidy/Column-renaming/Column-type-casting
    * Using functions to clean data
    * Clean separately -> Combine
    * Combine -> Clean the entire dataframe
13. Splitting columns meaningfully
    * split a string -> into multiple columns
14. Proper examples of TIDY data
15. melt, pivot, pivot_table, stack, unstack
    * pivot and pivot_table use cases -> duplicate entries
    * melt <-> pivot - back and forth
    * pivot_table - experiment with different aggfunc use cases
    * pivot_table - margins in a dataframe
16. Combining datasets
    * Experiment with multiple file names with regex pattern matching
    * concat -> stitching together what was once a single dataset
    * merge -> separate dataframes which are related in some way - (one-to-one/many-to-one/one-to-many/many-to-many)
17. Testing the datasets with assert
    * A testing framework for data science related tasks?
18. Get number of missing vals + dtype of each column as a single dataframe
19. General function to read a file in chunks or read the first few chunks or the nth chunk.
20. Explicitly specify dtypes while reading a file.
21. A way to get preliminary information about a file like shape, column names, dtypes etc without reading entire file?
22. Various ways of slicing a DatetimeIndex or datetime column
23. Color converter/fetcher api to show most appropriate RGB/CMYK color values + visualizer for same
24. <span style="color: red">**IDEA**</span> : Parse youtube playlists and make a spotify playlist out of it.
25. Implement a function to rename index by row number.
26. Hierarchichal index
    * Stack/unstack
    * swapping levels along both axes
    * Renaming columns
    * subsetting - using slice
    * Can groupby be used with this?
27. groupby use cases - split-apply-combine
    * aggregations/transformations/more-complex-workflows
    * Custom aggregation functions
    * get a specific group
    * fill nan values in groups
    * multiple columns groupby
    * groupby based on any pandas series -  columnn of other df without concat
    * multi-grouby -> column + other series
    * nan in group keys?
    * A bit complex operations based on an algo in other groups
28. Create a DataFrame class
    * inherit from pd.DataFrame -> improved
    * create a dataframe from scratch


