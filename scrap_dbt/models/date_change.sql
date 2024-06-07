with base as (
    select
        id,
        split(listing_date, ' ') as split_col
    from housing
),

formatted as (
    select
        id,
        regexp_replace(split_col[1], '\.', '') as listing_day,
        split_col[2] as listing_month,
        date_part('year', current_date()) as listing_year
    from base
)

select * from formatted