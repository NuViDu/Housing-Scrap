with base as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Jan\.', '1') as listing_month
    from date_change

),

step_1 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Feb\.', '2') as listing_month
    from base

),

step_2 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Marz', '3') as listing_month
    from step_1

),

step_3 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Apr\.', '4') as listing_month
    from step_2

),

step_4 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Mai', '5') as listing_month
    from step_3

),

step_5 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Juni', '6') as listing_month
    from step_4

),

step_6 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Juli', '7') as listing_month
    from step_5

),

step_7 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Aug\.', '8') as listing_month
    from step_6

),

step_8 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Sept\.', '9') as listing_month
    from step_7

),

step_9 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Okt\.', '10') as listing_month
    from step_8

),

step_10 as (

    select
        id,
        listing_day,
        listing_year,
        regexp_replace(listing_month, 'Nov\.', '11') as listing_month
    from step_9

),

step_11 as (

    select
        id,
        listing_day,
        regexp_replace(listing_month, 'Dez\.', '12') as listing_month,
        listing_year
    from step_10

)

select
    *
from step_11