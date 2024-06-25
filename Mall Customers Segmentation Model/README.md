Mall Customers Segmentation Model
==============================

Develop machine learning model to segment customers into groups based on income and spending score

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
<h2>Project Scope:</h2>
<p>
    Malls are often indulged in the race to increase their customers and making sales. To achieve this task machine learning is being applied by many malls already.
    It is amazing to realize the fact that how machine learning can aid in such ambitions. The shopping malls make use of their customers’ data and develop ML models to target the right audience for right product marketing.
</p>

<h2>Your role:</h2>
<p>
    Mall Customer data is an interesting dataset that has hypothetical customer data. It puts you in the shoes of the owner of a supermarket. You have customer data, and on this basis of the data, you have to divide the customers into various groups.
</p>

<h2>Goal:</h2>
<p>
    Build an unsupervised clustering model to segment customers into correct groups.
</p>

<h2>Specifics:</h2>
<ul>
    <li><strong>Machine Learning task:</strong> Clustering model</li>
    <li><strong>Target variable:</strong> N/A</li>
    <li><strong>Input variables:</strong> Refer to data dictionary below</li>
    <li><strong>Success Criteria:</strong> Cannot be validated beforehand</li>
</ul>

<h2>Data Dictionary:</h2>
<ul>
    <li><strong>CustomerID:</strong> Unique ID assigned to the customer</li>
    <li><strong>Gender:</strong> Gender of the customer</li>
    <li><strong>Age:</strong> Age of the customer</li>
    <li><strong>Income:</strong> Annual Income of the customers in 1000 dollars</li>
    <li><strong>Spending_Score:</strong> Score assigned between 1-100 by the mall based on customer' spending behavior</li>
</ul>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
