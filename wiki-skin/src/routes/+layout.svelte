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

        width: 80%
        margin: 20px auto

    .sidebar
        float: right
        
        
    .content
        


</style>


<div class="body">
    <div class="content">
        <slot />
    </div>
    <div class="sidebar">
        <nav>
            <a href="/">home</a>
        </nav>
    </div>
    
    
    
</div>