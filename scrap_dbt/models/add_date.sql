with base as (
    select
        *,
        concat_ws('-', listing_year, listing_month, listing_day)::date as listing_date
    from month_transform
)

select
    *
from base