<style lang="sass">
    $col_01: #222831
    $col_02: #393E46
    $col_03: #00ADB5
    $col_04: #EEEEEE
    $col_warning: rgb(221, 115, 115)
    $col_04_alt: rgb(237, 227, 228)
    $col_nice_blue: rgb(110, 180, 209)

    nav
        background-color: $col_02
        color: $col_04
        padding: 10px
        margin: 0
        text-align: left

        a
            color: $col_04

    .body
        background-color: $col_04
        box-shadow: 0 0 1px rgba(0,0,0, .25)
        border-radius: 2px
        padding: 0

        width: 80%
        margin: 20px auto

    .content
        padding: 10px 20px
        


</style>


<div class="body container">
    <div class="columns col-gapless">
        <div class="content column col-8">
            <slot />
        </div>
        <div class="sidebar column col-4">
            <nav>
                <a href="/">home</a>
            </nav>
        </div>
    </div>
    
    
    
</div>