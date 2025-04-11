# ML Datasets 🫙

> Event datasets used for training machine learning models.

## Data Sources

For each supported language, learning events and assessment events are continuously uploaded from Android devices to the webapp database.

And those datasets are then downloaded to this repository in a [daily cron job](.github/workflows/download-datasets-daily.yml).

```mermaid
flowchart
    subgraph device [Android device]
        kukariri -- AssessmentEvents --> analytics@{ shape: cyl }
    
        subgraph sg_lit [Literacy apps]
        herufi
        vitabu
        etc_lit[...]
        end
        sg_lit -- LearningEvents --> analytics
    
        subgraph sg_num [Numeracy apps]
        nyas-space-quest
        nambari
        etc_num[...]
        end
        sg_num -- LearningEvents --> analytics
    end

    subgraph rest_api_hin [hin.elimu.ai]
        analytics-->webapp_hin[webapp]@{ shape: cyl }
    end
    webapp_hin-->ml-datasets

    subgraph rest_api_tgl [tgl.elimu.ai]
        webapp_tgl[webapp]@{ shape: cyl }
    end
    webapp_tgl-->ml-datasets

    subgraph rest_api_tha [tha.elimu.ai]
        webapp_tha[webapp]@{ shape: cyl }
    end
    webapp_tha-->ml-datasets

    subgraph rest_api_vie [vie.elimu.ai]
        webapp_vie[webapp]@{ shape: cyl }
    end
    webapp_vie-->ml-datasets

    click kukariri "https://github.com/elimu-ai/kukariri"
    click herufi "https://github.com/elimu-ai/herufi"
    click vitabu "https://github.com/elimu-ai/vitabu"
    click nyas-space-quest "https://github.com/elimu-ai/nyas-space-quest"
    click nambari "https://github.com/elimu-ai/nambari"
    click analytics "https://github.com/elimu-ai/analytics"
    click webapp_hin "https://github.com/elimu-ai/webapp"
    click webapp_tgl "https://github.com/elimu-ai/webapp"
    click webapp_tha "https://github.com/elimu-ai/webapp"
    click webapp_vie "https://github.com/elimu-ai/webapp"
```

## Machine Learning Operations (MLOps)

When machine learning models are being trained with datasets collected from the elimu.ai Android apps, they should be fetching the data from this repository.

## Daily Updates

You can expect the datasets in this repository to be updated once per day.

> [!TIP]
> Since datasets in this repository are continuously updated, you should also design your machine learning code to continulously train new versions of your model (e.g. once per night).

## Code Usage

Prerequisites:

- Install [Python](https://www.python.org/)

### Dependencies

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

### Run

Download datasets:

```bash
python download_datasets.py
```

---

<p align="center">
  <img src="https://github.com/elimu-ai/webapp/blob/main/src/main/webapp/static/img/logo-text-256x78.png" />
</p>
<p align="center">
  elimu.ai - Free open-source learning software for out-of-school children 🚀✨
</p>
<p align="center">
  <a href="https://elimu.ai">Website 🌐</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki#readme">Wiki 📃</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/orgs/elimu-ai/projects?query=is%3Aopen">Projects 👩🏽‍💻</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki/milestones">Milestones 🎯</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki#open-source-community">Community 👋🏽</a>
  &nbsp;•&nbsp;
  <a href="https://www.drips.network/app/drip-lists/41305178594442616889778610143373288091511468151140966646158126636698">Support 💜</a>
</p>
