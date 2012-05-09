# Basic exec-capture tests

use Test::More;
use Test::Files;
use File::Path qw(remove_tree);
use IPC::Run3;
use FindBin qw($Bin);

my $dir = "$Bin/t01";

if (-d "$dir") {
  remove_tree("$dir") or die "remove_tree failed: $!";
}

ok(run3([ "$Bin/../exec-capture", '-d', $dir, '-N', 'echo1', qw(echo one two three) ]), "run ok");
ok(-f "$dir/echo1", 'output file echo1 created');
file_ok("$dir/echo1", "one two three\n", 'echo1 file contains correct output');

done_testing;

