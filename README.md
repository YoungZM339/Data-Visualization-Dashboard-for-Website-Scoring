# Website Scoring Dashboard

A website-scoring data-visualization prototype. The Django REST backend handles uploads and task records, while Vue 2, Element UI, ECharts, and DataV present website-experience metrics, a large-screen dashboard, and optimization suggestions.

## Feature Scope

- JWT login and user-related endpoints.
- Data uploads and processing tasks.
- Task records and result inspection.
- Website-experience dashboard.
- Large-screen data display.
- Static optimization-suggestion page.

## Metrics Displayed

Frontend components cover user experience, bounce rate, loading/network feedback, input delay, click/page errors, blank-screen metrics, and total/average scores. The exact fields, calculation definitions, and data quality depend on the backend algorithms and actual data source.

## Technology Stack

- Backend: Django 5, Django REST Framework, Simple JWT, pandas, and PyMySQL.
- Frontend: Vue 2, Vue CLI, Element UI, ECharts, and DataV.

## Local Development

Backend:

    cd backend/web_scoring
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Frontend:

    cd frontend
    npm install
    npm run dev

Before running migrations or tasks, review and configure your own database, data-query source, CORS policy, and service URLs. Placeholder or development settings from the repository must not connect directly to production data.

## Result Boundaries

Dashboard scores and optimization suggestions visualize and process the connected data; they are not a general website-performance certification. Before using the results for business or technical decisions, verify:

- Metric definitions and time windows;
- Data-collection completeness;
- Sample representativeness;
- Algorithm and rule versions;
- Consistency with original logs or monitoring systems.

## License

See the repository's LICENSE file.